# AI Money Stack for Indie Builders

5 local-first tools for indie builders who use AI agents like Codex and Claude Code.

## The Backstory

I asked an AI coding agent to autonomously generate revenue for 3 days. It made $0.

Every safety gate ("agent must not create accounts", "agent must not enter KYC", "agent must not cold email") blocked the last 5% of every revenue chain. But the agent DID finish 5 working tools.

This repo contains:
- **Free**: demos, samples, README, screenshots for all 5 tools
- **Paid bundle ($25 USD direct)**: source code, local PWA, checklists, examples, and ZIP delivery

## What's In The Bundle

| Tool | What It Does | LOC |
|---|---|---|
| Obsidian Revenue Scout CLI | Scans an Obsidian vault, scores notes by execution feasibility, outputs ranked action lists | 379 Python |
| Idea Forge PWA | Local browser app for trend-pattern remixing | 32 HTML/JS |
| PR Review Agent Lite | Deterministic PR review generator using `git`/`gh`-style local diffs - no LLM API calls | 42 Python |
| Obsidian-to-Money Endpoint Packet | Markdown reference mapping note patterns to monetization endpoints | docs |
| Paid OSS Bounty Quality Checklist | Filter rules built from 100+ rejected bounty candidates | docs |

## Free Demo

```bash
git clone https://github.com/duct-tape2/ai-money-stack.git
cd ai-money-stack
./demo.sh
```

This runs the Obsidian Revenue Scout's demo command against a fixture vault and shows the output format.

Prefer a quick look first? Download the release preview files:
- [immediate_actions.md](https://github.com/duct-tape2/ai-money-stack/releases/download/v1.0-free-preview/immediate_actions.md)
- [scan_report.md](https://github.com/duct-tape2/ai-money-stack/releases/download/v1.0-free-preview/scan_report.md)

## Get The Full Bundle ($25)

Three options:

### PayPal / Wise (International)
Pay direct with PayPal.Me: https://www.paypal.me/sks7178/25

Then email `sks7178@gmail.com` with payer name/email prefix, payment time, and the email address where you want the ZIP delivered.

If you prefer GitHub, open a buy issue with public-safe confirmation details only. Do not post the full PayPal transaction ID in a public issue: https://github.com/duct-tape2/ai-money-stack/issues/new?template=buy-bundle.yml

ZIP link is sent within 5 min during KST business hours.

## Done-For-You Setup ($99)

Want this same buyer-ready setup for your own GitHub repo or small digital product?

I can turn one existing repo/product into a simple sales page with:

- GitHub Pages landing copy
- payment CTA and public-safe buyer inquiry flow
- free preview/sample asset
- README polish
- delivery checklist
- link and release sanity check

Fixed price: **$99 USD** for one repo/product.  
Email `sks7178@gmail.com` with your repo URL and the words `repo-to-revenue setup`.

## Why $25

Individual tool prices: $19 + $29 + $19 + $9 + $9 = $85.
Direct bundle is 70% off because there is no marketplace fee, no hosted SaaS, and delivery is manual.

## Honest Limits

- These tools do NOT guarantee revenue. They reduce friction.
- You still need to file the PR, publish the product, talk to buyers.
- The scoring is a heuristic, not a prediction.

## Who This Is For

- Solo builders with large Obsidian or Notion vaults
- Indie hackers using Codex, Claude Code, or Cursor
- OSS maintainers and bounty contributors
- People tired of "agent must not" gates blocking real work

## Who This Is NOT For

- Enterprise teams (no SSO, no audit logs)
- Non-developers (CLI/Python required)

## 한국 중소기업용: Private AI Starter Kit (₩99,000)

> 직원 20-100명 제조/유통/백오피스 운영팀을 위한 로컬 AI 스타터킷

### 문제
- 사내 문서는 많은데 AI 담당자가 없다
- 외부 SaaS에 사내 자료를 올리기 어렵다 (보안/규정)
- 구축 대행을 부르면 수천만원이고 학습/유지보수가 곤란하다

### 솔루션
이 번들 + Mac mini/Studio 또는 사내 서버 1대로 사내 문서 검색/요약용 로컬 LLM을 빠르게 올린다. 외부 API 키, 토큰, 클라우드 업로드 없음. 모든 데이터가 사내에 머문다.

### 가격
- **Starter ₩99,000**: 파일형 상품 (5개 도구 + written quickstart + 샘플 문서 3개)
- **Team ₩390,000**: 설치 패키지 선주문 (위 + 업종별 customization 30분 + 30일 이메일 지원)
- **Enterprise**: 별도 문의

### 결제
1. 계좌이체 또는 Toss로 ₩99,000 입금 (계좌번호는 이메일 `sks7178@gmail.com` 또는 [Issue 열기](https://github.com/duct-tape2/ai-money-stack/issues/new?template=buy-bundle.yml))
2. 이메일로 입금자명, 입금시각, 배송받을 이메일을 보내기
3. 입금 확인 후 5분 내 ZIP 링크 + written quickstart 발송

### 포함
- 5개 도구 전체 소스 (un-obfuscated)
- 로컬 LLM quickstart 문서 (Ollama 확장용)
- 샘플 문서 3개 (제조/유통/백오피스)
- 한국어 README + written setup guide
- 14일 환불 보장

### Why It Works
- Mac Studio/mini는 60-90만원 (또는 이미 보유)
- 신규 SaaS 구독 0원
- 사내 데이터 외부 전송 0%
- 업종별 customization 가이드 포함

---

## Refund Policy

Full refund within 14 days if the tools don't run on your Mac (M1/M2/M3 or Intel, macOS 13+).

## Contact

Email `sks7178@gmail.com`, open an issue, or DM [@duct-tape2](https://github.com/duct-tape2) on GitHub.

---

Built by [@duct-tape2](https://github.com/duct-tape2). Made during a 3-day experiment in agent-autonomous revenue generation.
