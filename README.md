# AI Money Stack for Indie Builders

5 local-first tools plus a safe daily revenue routine for indie builders who use AI agents like Codex and Claude Code.

## The Backstory

I asked an AI coding agent to autonomously generate revenue for 3 days. It made $0.

Every safety gate ("agent must not create accounts", "agent must not enter KYC", "agent must not cold email") blocked the last 5% of every revenue chain. But the agent DID finish 5 working tools and a repeatable safe revenue operating loop.

This repo contains:
- **Free**: demos, samples, README, screenshots for all 5 tools
- **Free**: `storefront_checker.py` to audit buyer-readiness on any small product page
- **Paid bundle ($25 USD direct)**: source code, local PWA, checklists, daily routine, examples, and ZIP delivery

Direct checkout for AI Money Stack and all current offers:
https://duct-tape2.github.io/buy/

Not sure what to buy? Use the offer chooser:
https://duct-tape2.github.io/tools/offer-chooser/

If the free preview or checker helped and you do not need the paid bundle yet, a $5 thank-you tip is here:
https://www.paypal.me/sks7178/5

Bundle option:
Repo-to-Revenue Launch Bundle ($39) includes AI Money Stack plus GitHub Pages Storefront Starter.
https://duct-tape2.github.io/repo-to-revenue-launch-bundle/

## What's In The Bundle

| Tool | What It Does | LOC |
|---|---|---|
| Obsidian Revenue Scout CLI | Scans an Obsidian vault, scores notes by execution feasibility, outputs ranked action lists | 379 Python |
| Idea Forge PWA | Local browser app for trend-pattern remixing | 32 HTML/JS |
| PR Review Agent Lite | Deterministic PR review generator using `git`/`gh`-style local diffs - no LLM API calls | 42 Python |
| Obsidian-to-Money Endpoint Packet | Markdown reference mapping note patterns to monetization endpoints | docs |
| Paid OSS Bounty Quality Checklist | Filter rules built from 100+ rejected bounty candidates | docs |
| Safe Daily Revenue Routine | A 20-minute loop for checking real money signals, account gates, product health, and safe prize/bounty scans without drifting into unsafe work | docs |

## Free Demo

```bash
git clone https://github.com/duct-tape2/ai-money-stack.git
cd ai-money-stack
./demo.sh
```

This runs the Obsidian Revenue Scout's demo command against a fixture vault and shows the output format.

Prefer a quick look first? Download the release preview files:
- [live sample output preview](https://duct-tape2.github.io/examples/ai-money-stack-sample-output/)
- [immediate_actions.md](https://github.com/duct-tape2/ai-money-stack/releases/download/v1.0-free-preview/immediate_actions.md)
- [scan_report.md](https://github.com/duct-tape2/ai-money-stack/releases/download/v1.0-free-preview/scan_report.md)

## Free Storefront Checker

Before paying for the bundle or the done-for-you service, run the free checker against your own product page:

```bash
python3 storefront_checker.py https://yourname.github.io/your-product/
```

Sample report: [storefront_check_ai_money_stack.md](examples/sample-output/storefront_check_ai_money_stack.md)

It checks the signals that make a tiny digital-product page safer to buy from:

- page HTTP status
- title and description
- social card image
- payment link
- support email
- free sample or preview link
- refund/support language
- public-safe buyer contact path

If the report has `FAIL` or `WARN` items and you want me to fix the page for you, use the $99 repo-to-revenue setup below.

If you want to fix it yourself first, use the $19 DIY kit:

- Use the free GitHub template: https://github.com/new?template_name=github-pages-storefront-starter&template_owner=duct-tape2
- Add static PayPal checkout safely: https://duct-tape2.github.io/guides/paypal-static-storefront/
- Generate a full static storefront page, Product schema, checkout URL, and delivery mailto: https://duct-tape2.github.io/tools/static-storefront-builder/
- Generate a PayPal button, delivery email note, and HTML checkout block: https://duct-tape2.github.io/tools/paypal-button-builder/
- Request public-safe storefront feedback: https://github.com/duct-tape2/github-pages-storefront-starter/issues/new?template=storefront-feedback.yml
- GitHub Pages Storefront Starter: https://duct-tape2.github.io/storefront-starter/
- Free sample checklist: https://duct-tape2.github.io/storefront-starter/free-checklist.md?sample=1

## Get The Full Bundle ($25)

Three options:

### Instant Download Store
Buy the bundle here: https://payhip.com/b/RJ63W

### Payment and delivery
Payhip handles payment and ZIP delivery automatically. If you also want the GitHub Pages Storefront Starter kit, use the $39 launch bundle instead:
https://payhip.com/b/qHsNi

The active bundle checkout is:
https://payhip.com/b/qHsNi

If delivery fails, email `sks7178@gmail.com` with the product name and delivery email. Do not post private payment details in a public issue.

If you prefer GitHub, open a buy issue with public-safe confirmation details only. Do not post the full PayPal transaction ID in a public issue: https://github.com/duct-tape2/ai-money-stack/issues/new?template=buy-bundle.yml

The Payhip checkout above delivers the ZIP automatically.

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

- Service page: https://duct-tape2.github.io/ai-money-stack/repo-to-revenue/
- Ready to book directly: https://payhip.com/b/ZOl1I
- Open a public-safe inquiry: https://github.com/duct-tape2/ai-money-stack/issues/new?template=repo-to-revenue-setup.yml
- Booking terms: refund if I cannot deliver the scoped setup; one small correction pass within 7 days after delivery.

If the repo/product is private, email `sks7178@gmail.com` with your repo URL and the words `repo-to-revenue setup`.

## Why $25

Individual tool prices: $19 + $29 + $19 + $9 + $9 plus the routine template = $85+.
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
