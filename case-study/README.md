# Case Studies: 3 Days of Autonomous Agent Revenue Attempts

Raw data from a 72-hour autonomous agent experiment. Useful as reference for anyone trying similar work.

## What's Here

1. **[Bounty Search Failure Patterns](01-bounty-search-failure-patterns.md)** - Why 61 OSS bounty candidates all failed the Revenue Gate. Specific blocker categorization with counts.

2. **[Money Blocker Report](02-money-blocker-report.md)** - Comprehensive analysis of why $645 in submitted PRs sat unpaid. Maintainer review timing, claim flow gaps, Obsidian Revenue Scout monetization blocker.

3. **[Honest Report: What Agent Cannot Do Without You](03-honest-report-what-agent-cannot-do.md)** - Structural limits of autonomous revenue generation. The five identity gates (KYC, accounts, OAuth, social posting, payment endpoints) that no agent can cross.

## Key Numbers

- 72 hours of autonomous agent runtime
- 100+ paid OSS bounty candidates reviewed
- 0 Revenue Gate passes from the initial 61 candidates
- 6 PRs eventually submitted ($645 pipeline)
- $0 confirmed revenue
- 5 working tools shipped to disk
- 0 payment endpoints autonomously activated
- 5 minutes user time required to unblock all five gates

## Categorization Of Failure Modes

From the bounty failure analysis, the top blockers were:

| Blocker | Count (of 61 candidates) |
|---|---:|
| `competition_level=high` (duplicate PRs already open) | 44 |
| `account_needed_before_submission=true` | 27 |
| `testability=low` or `none` | 19 |
| `security_risk=medium` or `high` | 16 |
| `token_needed=true` | 8 |
| `paid_api_needed=true` | 4 |
| `merged_resolution_exists=true` | 2 |

The dominant blocker was NOT reward size. It was:
- duplicate active PR queues (44/61)
- account/platform gating (27/61)

## Why This Matters For Your Setup

If you're considering running an autonomous agent for revenue, save yourself 72 hours by understanding these categories upfront. Don't have your agent submit PRs to repos with `competition_level=high`. Don't have it pursue bounties that require account creation before submission.

The five-tool bundle in the parent repo includes a **Paid OSS Bounty Quality Checklist** that codifies these failure patterns into a pre-submission filter. ($9 individually, included in the $39 bundle.)

## Methodology Notes

- Agent: OpenAI Codex
- Runtime environment: Mac Studio with full file/git access
- GitHub OAuth: pre-authorized via gh CLI
- Capital: $1000 pre-approved for ads/SaaS infrastructure
- Single goal: "generate revenue autonomously"
- Safety policy: standard - no account creation, no KYC, no cold outreach

The agent was given maximum agency within those safety bounds. The bottleneck was structural, not effort.
