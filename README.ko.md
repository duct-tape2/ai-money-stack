# AI 머니 스택 (Private AI Starter Kit)

> 직원 20-100명 한국 중소기업 (제조/유통/백오피스)을 위한 로컬 AI 스타터킷

[English README](README.md) | 한국어

## 문제

- 사내 문서가 수백~수천 개인데 AI 전담자가 없다
- 외부 SaaS(ChatGPT, Claude API 등)에 사내 자료를 올리기 어렵다 (보안/규정/약관)
- 구축 대행을 부르면 3천만원 이상이고 학습/유지보수가 곤란하다
- 사내 직원 한 명도 AI 도구를 만들 시간이 없다

## 솔루션

이 번들 + Mac mini/Studio 또는 사내 서버 1대로 사내 문서 검색/요약용 로컬 LLM을 빠르게 올린다. 외부 API 키, 토큰, 클라우드 업로드 없음. 모든 데이터가 사내에 머문다.

## 가격

### Starter ₩99,000 (파일형 상품)
- 5개 도구 전체 소스 (Python/JS, un-obfuscated)
- 로컬 LLM quickstart 문서 (Ollama 확장용)
- 샘플 문서 3개 (제조/유통/백오피스)
- 한국어 README + written setup guide
- 14일 환불 보장

### Team ₩390,000 (설치 패키지 + 지원)
- Starter 전체
- 업종별 customization 30분 (영상 통화)
- 30일 이메일 지원
- 도입 체크리스트
- 14일 환불 보장

### Enterprise (별도 문의)
- 위 전체 + 현장 방문 1회
- 60일 지원
- 사내 교육 1회 (2시간)

## 결제

### 한국 (계좌이체 / Toss)
1. [GitHub Issue 열기](https://github.com/duct-tape2/ai-money-stack/issues/new?template=buy-bundle.yml)에서 구매 신청 (Region: Korea 선택)
2. 24시간 내 입금 계좌 정보 DM
3. ₩99,000 (Starter) 또는 ₩390,000 (Team) 입금
4. 입금 확인 후 5분 내 ZIP 링크 + written quickstart DM

### 해외 (PayPal)
- $25 USD (AI Money Stack direct bundle) 또는 $79 USD (Private AI Starter Kit)을 PayPal.Me로 송금
- [GitHub Issue](https://github.com/duct-tape2/ai-money-stack/issues/new?template=buy-bundle.yml)에 transaction ID 적기

## 포함된 5개 도구

1. **Obsidian Revenue Scout CLI** (₩40,000 상당)
   - 로컬 Markdown/Obsidian 폴더 스캔
   - 수익 가능성 자동 스코어링
   - 즉시 실행 가능한 액션 리스트 출력

2. **Idea Forge PWA** (₩40,000 상당)
   - 모바일 설치 가능 PWA
   - 트렌드 → 본인 제품 가설 변환
   - 카피라이트 안전

3. **PR Review Agent Lite** (₩30,000 상당)
   - GitHub gh CLI 기반
   - LLM API 호출 없음 (비용 0)
   - 일관된 PR 리뷰 템플릿

4. **노트→결제 endpoint 패킷** (₩15,000 상당)
   - 노트 패턴 → 수익 endpoint 매핑
   - 한국 결제 옵션 포함

5. **OSS 바운티 필터 체크리스트** (₩15,000 상당)
   - 100+ 거절 후보 분석 기반
   - 시간 낭비 방지 룰

## 왜 ₩99,000이 합리적인가

- 개별 도구 합계: ₩140,000
- 번들 ₩99,000 = 29% 할인
- 시간 단축: 사내 스크래치 빌드 = 20-40시간 = ₩2,000,000+ 인건비
- 즉시 실행 가능: 다운로드 후 1시간 내 데모 가능

## 환불

다운로드 후 14일 내, Mac (M1/M2/M3 또는 Intel)에서 데모 실행 실패 시 전액 환불.

## 누구를 위한 것이 아닌가

- 비개발자 (CLI/Python 기초 필요)
- SSO/감사 로그 필요한 대기업
- "AI가 알아서 모든 걸 해결" 기대하는 사람

## FAQ

**Q. Mac Studio가 꼭 필요한가?**
A. 아니다. Mac mini M2 (32GB RAM)도 충분. 사내 Linux 서버도 OK.

**Q. 어떤 LLM 모델을 사용하나?**
A. Ollama로 Llama 3.1 8B, Qwen2.5, gemma2 등 무료 모델. 가이드 포함.

**Q. 한국어 문서도 잘 되나?**
A. Qwen2.5와 Llama 3.1은 한국어 지원. 샘플 문서에 한국어 포함.

**Q. 환불 정책은?**
A. 14일 내 데모 실행 실패하면 전액. 단순 변심도 7일 내 50% 환불.

**Q. 업종 customization 어디까지 가능한가?**
A. Team tier 30분 통화에서 사내 문서 1-2개 기준 prompt template + chunking strategy 잡아드림.

## 연락처

- GitHub Issue: https://github.com/duct-tape2/ai-money-stack/issues
- 이메일: sks7178@gmail.com
- 응답 시간: 24시간 (KST 영업일)

---

만든 사람: [@duct-tape2](https://github.com/duct-tape2). 3일 자율 AI 에이전트 수익 생성 실험의 부산물.
