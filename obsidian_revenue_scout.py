#!/usr/bin/env python3
"""Rank Obsidian notes by near-term revenue execution feasibility."""

from __future__ import annotations

import argparse
import csv
import re
from dataclasses import dataclass
from pathlib import Path


MONEY_PATTERNS = [
    (r"\$(\d+(?:\.\d+)?)", 1.0),
    (r"reward:\s*\$?(\d+(?:\.\d+)?)", 1.0),
    (r"price:\s*\$?(\d+(?:\.\d+)?)", 1.0),
    (r"(\d{2,})\s*usd", 1.0),
]

BLOCKER_WORDS = {
    "kyc",
    "oauth",
    "stripe",
    "developer account",
    "app store",
    "marketplace",
    "ads",
    "captcha",
    "paid api",
    "token",
    "secret",
    "bank",
    "cold email",
}

GO_WORDS = {
    "local",
    "cli",
    "readme",
    "sample output",
    "tests",
    "github",
    "bounty",
    "template",
    "markdown",
    "no external account",
    "no paid api",
    "no token",
}


@dataclass
class Idea:
    title: str
    source_note_path: str
    original_summary: str
    monetization_route: str
    immediate_action: str
    estimated_hours: float
    possible_revenue_usd: float
    confirmed_revenue_probability_this_month: float
    external_account_needed: bool
    paid_api_needed: bool
    token_or_secret_needed: bool
    user_effort_needed: str
    agent_can_execute_now: bool
    automation_potential: int
    blocker: str
    score: float
    next_action: str
    differentiation_angle: str


def clean_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip() or fallback
    return fallback


def summarize(text: str, max_lines: int = 4) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return " / ".join(lines[:max_lines])[:360]


def find_money(text: str) -> float:
    lowered = text.lower()
    values: list[float] = []
    for pattern, multiplier in MONEY_PATTERNS:
        for match in re.finditer(pattern, lowered):
            try:
                values.append(float(match.group(1)) * multiplier)
            except ValueError:
                pass
    if values:
        return max(values)
    if "bundle" in lowered or "template" in lowered or "tool" in lowered:
        return 19.0
    return 9.0


def route_for(text: str) -> str:
    lowered = text.lower()
    if "bounty" in lowered or re.search(r"\bpr\b|pull request", lowered):
        return "paid_oss_bounty"
    if "cli" in lowered or "script" in lowered:
        return "CLI_tool"
    if "template" in lowered or "pack" in lowered:
        return "template_pack"
    return "developer_asset"


def blocker_for(text: str) -> str:
    lowered = text.lower()
    hits = sorted(word for word in BLOCKER_WORDS if word in lowered)
    if "no paid api" in lowered:
        hits = [hit for hit in hits if hit != "paid api"]
    if "no token" in lowered or "token needed" in lowered:
        hits = [hit for hit in hits if hit != "token"]
    if "no secret" in lowered:
        hits = [hit for hit in hits if hit != "secret"]
    if "no external account" in lowered:
        hits = [hit for hit in hits if hit not in {"oauth", "kyc", "developer account", "marketplace", "bank", "stripe"}]
    if hits:
        if any(hit in hits for hit in ("app store", "developer account", "marketplace", "oauth", "kyc", "stripe", "bank")):
            return "external account/payment/marketplace step"
        if any(hit in hits for hit in ("paid api", "token", "secret")):
            return "paid API/token/secret required"
        return ", ".join(hits[:3])
    return "none for local MVP"


def immediate_action_for(route: str, blocked: bool) -> str:
    if blocked:
        return "do not execute until blocker is cleared"
    if route == "paid_oss_bounty":
        return "verify issue freshness, implement minimal PR, test, submit with one claim"
    if route == "CLI_tool":
        return "build a local CLI with README, demo, tests, and sample output"
    if route == "template_pack":
        return "package as markdown templates with examples and a small landing page"
    return "turn the note into a small local-first asset with demo output"


def estimate_hours(text: str) -> float:
    lowered = text.lower()
    hours = 3.0
    if "small" in lowered or "readme" in lowered:
        hours -= 0.5
    if "app store" in lowered or "marketplace" in lowered:
        hours += 2.0
    if "tests" in lowered or "cli" in lowered:
        hours += 0.5
    return max(1.0, min(8.0, hours))


def probability_for(text: str, blocked: bool, route: str) -> float:
    if blocked:
        return 0.05
    lowered = text.lower()
    probability = 0.08
    probability += sum(0.015 for word in GO_WORDS if word in lowered)
    if route == "paid_oss_bounty":
        probability += 0.16
    if "reward" in lowered or "$" in lowered:
        probability += 0.08
    return round(min(probability, 0.45), 2)


def score_idea(revenue: float, probability: float, hours: float, blocked: bool, automation: int) -> float:
    score = (revenue * probability * 10.0) / max(hours, 1.0)
    score += automation * 3.0
    if blocked:
        score -= 35.0
    return round(score, 2)


def analyze_note(path: Path, vault: Path) -> Idea:
    text = path.read_text(encoding="utf-8", errors="replace")
    rel_path = str(path.relative_to(vault))
    title = clean_title(text, path.stem.replace("_", " ").title())
    route = route_for(text)
    blocker = blocker_for(text)
    blocked = blocker != "none for local MVP"
    revenue = find_money(text)
    hours = estimate_hours(text)
    probability = probability_for(text, blocked, route)
    automation = 5 if "cli" in text.lower() or "local" in text.lower() else 4
    score = score_idea(revenue, probability, hours, blocked, automation)
    action = immediate_action_for(route, blocked)
    if blocked:
        next_action = action
    else:
        next_action = action
    return Idea(
        title=title,
        source_note_path=rel_path,
        original_summary=summarize(text),
        monetization_route=route,
        immediate_action=action,
        estimated_hours=hours,
        possible_revenue_usd=revenue,
        confirmed_revenue_probability_this_month=probability,
        external_account_needed=blocked and "external account" in blocker,
        paid_api_needed="paid API" in blocker,
        token_or_secret_needed="token" in blocker or "secret" in blocker,
        user_effort_needed="none for local MVP" if not blocked else "human approval/setup likely needed",
        agent_can_execute_now=not blocked,
        automation_potential=automation,
        blocker=blocker,
        score=score,
        next_action=next_action,
        differentiation_angle=(
            "quality PR with transparent AI assistance and low maintainer review cost"
            if route == "paid_oss_bounty"
            else "offline, no paid API, redaction-first, reproducible demo"
        ),
    )


def discover_notes(vault: Path) -> list[Path]:
    return sorted(path for path in vault.rglob("*.md") if path.is_file())


def write_csv(ideas: list[Idea], out: Path) -> None:
    fields = [
        "idea_title",
        "source_note_path",
        "monetization_route",
        "estimated_hours",
        "possible_revenue_usd",
        "confirmed_revenue_probability_this_month",
        "agent_can_execute_now",
        "blocker",
        "score",
        "next_action",
    ]
    with (out / "ideas.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for idea in ideas:
            writer.writerow(
                {
                    "idea_title": idea.title,
                    "source_note_path": idea.source_note_path,
                    "monetization_route": idea.monetization_route,
                    "estimated_hours": idea.estimated_hours,
                    "possible_revenue_usd": idea.possible_revenue_usd,
                    "confirmed_revenue_probability_this_month": idea.confirmed_revenue_probability_this_month,
                    "agent_can_execute_now": str(idea.agent_can_execute_now).lower(),
                    "blocker": idea.blocker,
                    "score": idea.score,
                    "next_action": idea.next_action,
                }
            )


def write_scan_report(ideas: list[Idea], out: Path) -> None:
    go_count = sum(1 for idea in ideas if idea.agent_can_execute_now)
    lines = [
        "# Obsidian Revenue Scout Scan Report",
        "",
        f"- notes_scanned: {len(ideas)}",
        f"- go_candidates: {go_count}",
        f"- no_go_candidates: {len(ideas) - go_count}",
        "",
        "## Top Candidates",
    ]
    for idea in ideas[:10]:
        lines.extend(
            [
                "",
                f"### {idea.title}",
                f"- source: `{idea.source_note_path}`",
                f"- route: {idea.monetization_route}",
                f"- score: {idea.score}",
                f"- next_action: {idea.next_action}",
                f"- blocker: {idea.blocker}",
            ]
        )
    (out / "scan_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_immediate_actions(ideas: list[Idea], out: Path) -> None:
    go = [idea for idea in ideas if idea.agent_can_execute_now]
    no_go = [idea for idea in ideas if not idea.agent_can_execute_now]
    lines = ["# Obsidian Immediate Actions", "", "## Go Candidates", ""]
    for idea in go:
        lines.extend(
            [
                f"- {idea.title}",
                f"  - score: {idea.score}",
                f"  - route: {idea.monetization_route}",
                f"  - action: {idea.next_action}",
                f"  - source: `{idea.source_note_path}`",
            ]
        )
    lines.extend(["", "## No-Go Or Human-Action Candidates", ""])
    for idea in no_go:
        lines.extend(
            [
                f"- {idea.title}",
                f"  - score: {idea.score}",
                f"  - blocker: {idea.blocker}",
                f"  - source: `{idea.source_note_path}`",
            ]
        )
    (out / "immediate_actions.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_pipeline(ideas: list[Idea], out: Path) -> None:
    lines = ["# Obsidian Idea Pipeline", ""]
    for idea in ideas:
        lines.extend(
            [
                f"## {idea.title}",
                "",
                f"- idea_title: {idea.title}",
                f"- source_note_path: `{idea.source_note_path}`",
                f"- original_summary: {idea.original_summary}",
                f"- monetization_route: {idea.monetization_route}",
                f"- immediate_action: {idea.immediate_action}",
                f"- estimated_hours: {idea.estimated_hours}",
                f"- possible_revenue_usd: {idea.possible_revenue_usd}",
                f"- confirmed_revenue_probability_this_month: {idea.confirmed_revenue_probability_this_month}",
                f"- external_account_needed: {str(idea.external_account_needed).lower()}",
                f"- paid_api_needed: {str(idea.paid_api_needed).lower()}",
                f"- token_or_secret_needed: {str(idea.token_or_secret_needed).lower()}",
                "- legal_risk: low",
                "- spam_risk: low",
                f"- user_effort_needed: {idea.user_effort_needed}",
                f"- agent_can_execute_now: {str(idea.agent_can_execute_now).lower()}",
                f"- automation_potential: {idea.automation_potential}",
                f"- differentiation_angle: {idea.differentiation_angle}",
                "- expected_time_to_submit: same day",
                "- expected_time_to_payment: unknown until buyer/bounty accepts",
                f"- blocker: {idea.blocker}",
                f"- score: {idea.score}",
                f"- next_action: {idea.next_action}",
                "",
            ]
        )
    (out / "idea_pipeline.md").write_text("\n".join(lines), encoding="utf-8")


def write_goal(ideas: list[Idea], out: Path) -> None:
    executable = [idea for idea in ideas if idea.agent_can_execute_now]
    top = executable[0] if executable else ideas[0]
    text = (
        f"/goal Execute the single highest-scoring local revenue action: {top.title}. "
        f"Source note: {top.source_note_path}. Route: {top.monetization_route}. "
        f"Action: {top.next_action}. Do not use paid APIs, tokens, account creation, "
        "payment/KYC, cold outreach, or automated comments. Produce README, demo, "
        "sample output, pricing hypothesis, launch copy, tests, verification proof, "
        "and keep confirmed revenue separate from possible revenue.\n"
    )
    (out / "next_codex_goal.md").write_text(text, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--vault", type=Path, required=True, help="Obsidian vault or folder containing markdown notes")
    parser.add_argument("--out", type=Path, required=True, help="Output directory")
    parser.add_argument("--limit", type=int, default=10, help="Maximum candidates to write")
    args = parser.parse_args()

    if not args.vault.exists():
        raise SystemExit(f"Vault not found: {args.vault}")
    args.out.mkdir(parents=True, exist_ok=True)

    notes = discover_notes(args.vault)
    ideas = [analyze_note(path, args.vault) for path in notes]
    ideas.sort(key=lambda idea: idea.score, reverse=True)
    ideas = ideas[: args.limit]

    write_csv(ideas, args.out)
    write_scan_report(ideas, args.out)
    write_immediate_actions(ideas, args.out)
    write_pipeline(ideas, args.out)
    write_goal(ideas, args.out)

    print(f"Scanned {len(notes)} notes; wrote {len(ideas)} candidates to {args.out}")


if __name__ == "__main__":
    main()
