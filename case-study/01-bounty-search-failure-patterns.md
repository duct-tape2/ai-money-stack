# Bounty Search Failure Analysis

Updated: 2026-05-14 17:17 KST

## Inputs Reviewed

- Previous force search file: `OPPORTUNITY_PIPELINE_FORCE_2026-05-14.csv`
- Previous blocker report: `MONEY_BLOCKER_REPORT.md`
- Previous candidate count: 61
- Previous Revenue Gate pass count: 0
- Current submitted pipeline before this run: `$375`
- Current confirmed revenue before this run: `$0`

## Previous 61 Candidate Failure Pattern

- `competition_level=high` or `very_high`: 44 candidates
- `account_needed_before_submission=true`: 27 candidates
- `token_needed=true`: 8 candidates
- `paid_api_needed=true`: 4 candidates
- `testability=low` or `none`: 19 candidates
- `security_risk=medium` or `high`: 16 candidates
- `merged_resolution_exists=true` or `unknown`: 2 candidates

The dominant blocker was not only reward size. The largest blockers were duplicate active PR queues, account or platform gates, unclear payout paths, token/API requirements, and tasks that would require security-adjacent work or non-local proof.

## Overly Strict Conditions From The Previous Run

- Reward minimum `$30` filtered out micro bounties that may still count as submitted revenue.
- Time window `2-6 hours` filtered out some docs/test/example work that could take `6-12 hours`.
- Candidate type focused too much on code PRs and not enough on docs, tests, examples, README fixes, issue reproductions, sample outputs, config, dependency cleanup, or small GitHub Action work.
- Search platform focus was too narrow: Algora/Opire/IssueHunt misses maintainer-sponsored GitHub issues and micro-bounty repos.

## Relaxed Strategy For This Run

- Reward threshold lowered from `$30` to `$1`.
- Implementation window expanded from `2-6 hours` to `1-12 hours`.
- Candidate types expanded to docs, tests, examples, README, CLI, GitHub Action, template, sample output, issue reproduction, config, dependency cleanup, plugin, and developer tool.
- Search sources expanded to GitHub reward issues, maintainer-sponsored issues, README-stated rewards, symbolic-looking micro-bounties, and docs/test-specific reward issues.

## New Blocker Discovered During Micro Search

The main `$1` micro-bounty cluster was `UnsafeLabs/Bounty-Hunters`. It looked viable from labels and issue comments, but the cloned repo's `CONTRIBUTING.md` states that its bounties are symbolic, part of an academic study, reviewed for research only, and not the right repo for paid bounty work. That makes those `$1` issues invalid as submitted revenue endpoints even when issue labels show `$1`.

Other micro candidates failed for one or more of these reasons:

- test/demo payment flow rather than real payout
- duplicate active PRs already solving the same issue
- assigned or role-gated bounty
- token/points/non-USD reward instead of clear cash
- claim path requires an external account before submission
- screenshot/video or external-service proof requirement
- maintainer already selected a likely winner
- social engagement requirement that would violate the no-spam rule

## Decision

Do not submit a low-quality or duplicate PR just to increase a number. Since no safe direct paid endpoint passed the relaxed `$1+` gate, switch to Human Revenue Packets that convert existing Obsidian-derived assets into user-postable paid listings. These packets are not recorded as submitted revenue.
