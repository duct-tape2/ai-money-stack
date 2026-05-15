# Codex/Claude Code Autonomous Revenue Playbook

> What to do (and what NOT to do) when you set an AI agent loose with "make money autonomously"

Based on a 72-hour experiment that generated $0, plus follow-up structured handoff that produced live payment endpoints in 90 minutes.

## TL;DR

| Phase | Agent autonomy | Human time | Expected output |
|---|---|---|---|
| **Pre-flight (1 hour)** | High | 10 min | Identity-attestation list, scope boundaries |
| **Asset production (48-72 hours)** | Very high | 0 min | Working tools, ZIPs, source code |
| **Distribution scaffolding (6 hours)** | High | 5 min (URL paste) | Public repo, landing page, marketing copy |
| **Identity handoff (10 minutes)** | Low | 10 min | Payment endpoint live, account activated |
| **Outreach (ongoing)** | Medium | 30 sec - 5 min/day | Traffic, sales, conversions |

The key insight: **don't ask an agent to "make money." Ask it to produce every artifact required for you to make money in 5 minutes of click work.**

## The Five Identity Gates

Every autonomous revenue chain hits these in order:

### Gate 1: Payment Account Creation
**Examples**: Stripe, Lemon Squeezy, Polar.sh, Gumroad, Ko-fi
**Why agent can't pass**: KYC requires biometric/government ID assertion. Agent cannot legitimately claim to be a specific human.
**Workaround**: Pre-grant one specific email/handle as the payment endpoint. Agent uses only that element. Activated by user one-time (~60 seconds).

### Gate 2: OAuth To Existing Accounts
**Examples**: X/Twitter, LinkedIn, Reddit posting
**Why agent can't pass**: OAuth flow requires user's logged-in browser session for new app authorization. Agent operates headless.
**Workaround**: gh CLI is a special case - if pre-authenticated by user, agent can comment on issues and create repos. For other platforms, draft content for user to paste (30 seconds total).

### Gate 3: KYC For Payouts
**Examples**: GitHub Sponsors (Stripe Connect), Polar.sh payout
**Why agent can't pass**: Identity verification at receiving end.
**Workaround**: User activates one channel one-time. Subsequent receipts route through it automatically.

### Gate 4: Cold Outreach
**Examples**: DM/email to people not yet contacted
**Why agent can't pass (correctly)**: Spam prevention. Agent could but should not assume identity in unsolicited outbound messages.
**Workaround**: Helpful, relevant comments on public discussions where the user-authenticated account is already a participant. Not spam = legitimate contribution.

### Gate 5: Subscription Activation
**Examples**: Activating paid Claude/OpenAI API, Vercel/Railway deployment
**Why agent can't pass**: Payment method binding.
**Workaround**: User pre-funds capacity. Agent uses within budget.

## The 90-Minute Handoff Pattern (What Worked)

After 72 hours of $0 from pure autonomous mode, this 90-minute structured handoff produced:
- 2 public GitHub repos
- 2 live landing pages (HTTP 200)
- 1 payment endpoint live (PayPal email pasted in README)
- 6 PR follow-up comments sent
- 3 helpful comments on relevant OSS discussions
- 199-card Anki deck auto-generated
- Korean SMB tier (₩99,000 / ₩390,000) pricing live
- Bitcoin wallet generated (publish-pending verification)
- launchd hourly monitoring job

### The structure was:

1. **User authorizes one specific identity element** (in our case: one email as PayPal endpoint, gh CLI authenticated for comments)
2. **Agent builds the 95%** that doesn't need identity: source code, bundles, copy, landing pages, repos, automation
3. **User does the 10-second clicks** that do need identity: signing in to Polar, posting one tweet, opening a buy-bundle GitHub Issue
4. **Watcher script auto-updates content** when user fills payment info file

## Anti-Patterns To Avoid

### Anti-pattern 1: "Just figure out KYC"
Will burn agent time and produce nothing. KYC is a hard wall by design.

### Anti-pattern 2: "Try every platform"
Agent enumerates 10 platforms, accumulates 10 "needs account creation" blockers, ships nothing.
Fix: pick 1-2 platforms maximum, fully complete the user-action handoff for those.

### Anti-pattern 3: "Submit any PR"
Without quality filters, agent submits to repos with `competition_level=high` (44/61 candidates in our test) and gets ignored.
Fix: codify failure modes as pre-submission filter.

### Anti-pattern 4: "Autonomous social posting"
Agent without OAuth posts to its own throwaway accounts → no audience → no signal.
Fix: agent drafts content, user pastes.

### Anti-pattern 5: "Wait for organic traffic"
Without explicit distribution, public repos sit at 0 stars indefinitely.
Fix: helpful comments on relevant discussions (legitimate, low-friction) + at least one user-paste tweet.

## What Agents Are Great At

- Writing source code (200-1500 LOC tools shipped in 72h)
- Generating data assets (we built 199 vocabulary cards as a CSV → Anki deck)
- Drafting copy in multiple lengths/tones
- Filing structured PRs
- Sending polite follow-up comments
- Building monitoring/cron infrastructure (launchd plists)
- Translating content across languages
- Generating landing pages from templates

## What Agents Are Not Great At (Yet)

- Producing original creative work that resonates with a specific audience
- Knowing what will actually sell vs. what looks like it should
- Navigating ambiguous human-relationship cues (e.g., "the maintainer seems annoyed")
- Spotting legal/copyright edge cases reliably
- Making strategic abandonment decisions ("this product line won't work, kill it")

## Tool Stack Recommendation

If you're starting from scratch:

| Layer | Tool | Why |
|---|---|---|
| Local agent | Claude Code on Mac | gh CLI auth, file system access |
| Cloud agent | OpenAI Codex (browser) | Long-running tasks |
| Storage | Plain markdown in Obsidian vault | Agent-readable, human-readable |
| Distribution | GitHub repo + Pages | Free, agent can push |
| Payment endpoint | PayPal email (1 user click) | Lowest setup friction |
| Marketing surface | Helpful comments on GitHub Discussions | Legitimate, agent-capable |
| Monitoring | launchd cron + watcher scripts | Mac native |
| Backup payment | Polar.sh with Stripe Connect KR | Higher conversion later |

## The Real ROI Equation

For solo builders / indie hackers:

```
Revenue per month = (Agent-shipped products) × (Conversion rate) × (Traffic from distribution)
                  - (Time on identity-handoff clicks) × (Hourly opportunity cost)
                  - (Subscription/hosting costs)
```

In our case:
- Agent-shipped products: 2 (bundle, Anki pack)
- Conversion rate: untested, hypothetical 1-3%
- Traffic: 3 GitHub comments + 0 user-paste tweets (pending)
- Identity-handoff time: ~10 minutes total
- Hosting: $0 (GitHub Pages free)

Projected month-1 revenue: $39-300 (1-7 sales).

## Open Questions

These remain unsolved as of 2026-05-15:

1. Can an agent learn from a failed sale (refund request) and improve product copy autonomously?
2. Is there a clean way to grant "partial identity attestation" (one handle for receipts only, not for posting)?
3. What's the right ratio of agent-time to user-time for sustainable indie revenue?

If you have data points, open an issue or DM.
