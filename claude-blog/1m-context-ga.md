# 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

# 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

두 모델 모두 전체 100만 컨텍스트 창에 표준 요금이 적용되며, 장문 컨텍스트에 대한 추가 요금은 없습니다. 미디어 한도는 이미지 또는 PDF 페이지 기준 600개까지 확대됩니다.

‍

- 카테고리제품 발표엔터프라이즈 AI

- 제품Claude PlatformClaude Code

- 날짜2026-03-13

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/1m-context-ga

이제 Claude Platform에서 Claude Opus 4.6과 Sonnet 4.6은 전체 100만 컨텍스트 창을 표준 요금으로 제공합니다. Opus 4.6은 100만 토큰당 $5/$25, Sonnet 4.6은 $3/$15의 표준 요금이 전체 100만 창 전 구간에 동일하게 적용됩니다. 컨텍스트 길이에 따른 추가 과금은 없으며, 90만 토큰 요청도 9천 토큰 요청과 동일한 토큰당 비율로 청구됩니다.

정식 지원으로 새롭게 달라진 사항:

- 단일 요금으로 전체 컨텍스트 창을 이용할 수 있습니다.장문 컨텍스트에 대한 추가 요금은 없습니다.

- 모든 컨텍스트 길이에서 요청 한도가 그대로 적용됩니다.표준 계정의 처리량은 전체 컨텍스트 창 전반에 동일하게 적용됩니다.

- 요청당 미디어 한도가 6배 확대됩니다.이미지 또는 PDF 페이지를 기존 100개에서 최대 600개까지 지원합니다. 이 기능은 오늘부터 Claude Platform 기본 환경, Microsoft Foundry, Google Cloud의 Vertex AI에서 사용 가능합니다.

- 더 이상 베타 헤더가 필요하지 않습니다.20만 토큰을 초과하는 요청은 자동으로 처리됩니다. 이미 베타 헤더를 보내고 있는 경우에는 무시되므로, 코드를 변경할 필요가 없습니다.

이제 Max, Team, Enterprise 사용자는 Claude Code에서 Opus 4.6과 함께 100만 컨텍스트를 사용할 수 있습니다.Opus 4.6 세션에서는 전체 100만 컨텍스트 창이 자동으로 적용되어, 축약은 줄어들고, 더 많은 대화 내용이 그대로 유지됩니다. 이전에는 100만 컨텍스트를 사용하려면 추가 사용량이 필요했습니다.

### 제대로 작동하는 장문 컨텍스트

100만 토큰 컨텍스트는 모델이 필요한 정보를 정확히 기억하고, 이를 바탕으로 추론할 수 있을 때만 의미가 있습니다. Opus 4.6은 해댕 컨텍스트 길이의 MRCR v2에서 78.3%를 기록했으며, 이는 프론티어 모델 중 가장 높은 점수입니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b49c06e1c573f3ce50276b_image%20(3).png)

즉, 전체 코드베이스, 수천 페이지의 계약서, 또는 장시간 실행되는 에이전트의 전체 추적 기록(도구 호출, 관찰 결과, 중간 추론)을 불러와 그대로 활용할 수 있다는 의미입니다. 이전에 장문 컨텍스트 작업에 필요했던 엔지니어링 작업, 손실이 발생하는 요약, 컨텍스트 정리는 더 이상 필요하지 않습니다. 전체 대화가 그대로 유지됩니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad6788c7a1b711a85623_Ramp_light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/68b5ad62e2f100f80635f7a7_Ramp_dark.svg)

Claude Code는 Datadog, Braintrust, 데이터베이스, 소스 코드를 검색하는 데 100K가 넘는 토큰을 소비할 수 있습니다. 그러다 압축이 시작되면 세부 정보가 사라지고, 디버깅은 제자리를 맴돌게 됩니다. 1M 컨텍스트에서는 한 창 안에서 검색, 재검색, 엣지 케이스 집계, 수정안 제안까지 모두 처리합니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e943b167e62bb019de7_Logo_green.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b23e9850d979b6157caf78_Logo_white.svg)

Opus 4.6의 1M 컨텍스트 창이 나오기 전에는 사용자가 대용량 PDF, 데이터셋, 이미지를 불러오자마자 컨텍스트를 압축해야 했고, 그 결과 가장 중요한 작업에서 충실도를 잃었습니다. 이제는 압축 이벤트가 15% 감소했습니다. 저희 에이전트는 모든 것을 그대로 유지한 채 첫 페이지에서 읽은 내용을 잊지 않고 몇 시간 동안 실행됩니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a29deb8193497afd3b2cd24_brand-logo-cognition-black.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a29deb952fed1bad85c342c_brand-logo-cognition-white.svg)

1M 컨텍스트 창을 갖춘 Opus 4.6은 저희 Devin Review 에이전트를 훨씬 더 효과적으로 만들어 주었습니다. 200K 컨텍스트 창에는 대규모 diff가 들어가지 않아 에이전트가 컨텍스트를 분할 처리해야 했고, 이로 인해 더 많은 패스와 파일 간 종속성 손실이 발생했습니다. 1M 컨텍스트에서는 전체 diff를 한 번에 투입해, 더 단순하고 토큰 효율적인 하니스로도 더 높은 품질의 리뷰를 얻을 수 있습니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbdde1a3d17f2d9e91607_eve-light-mode.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69ebbde617bb08ba0d0157b8_eve-dark-mode.svg)

Eve는 1M 컨텍스트를 기본값으로 사용합니다. 원고 측 변호사들이 다루는 가장 어려운 문제들이 이를 요구하기 때문입니다. 400페이지 분량의 증언 녹취록을 상호 참조하는 일이든, 사건 파일 전체에서 핵심 연결고리를 찾아내는 일이든, 확장된 컨텍스트 창 덕분에 이전보다 훨씬 높은 품질의 답변을 제공할 수 있습니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b2420c325130a6b3466795_Physical%20Superintelligence%20Logo%20-%20Dark.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b24208d5bf1b81446a6ad3_Physical%20Superintelligence%20Logo%20-%20Light.svg)

과학적 발견에는 연구 문헌, 수학적 프레임워크, 데이터베이스, 시뮬레이션 코드를 동시에 아우르는 추론이 필요합니다. Claude Opus 4.6의 1M 컨텍스트와 확장된 미디어 한계 덕분에 저희 에이전틱 시스템은 수백 편의 논문, 증명, 코드베이스를 단일 패스로 종합할 수 있으며, 이를 통해 기초 및 응용 물리학 연구를 극적으로 가속화할 수 있습니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d248b84e40f85eca3f68_GC%20AI%20220px%20navy%20(1).png)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b1d24b433e03540b6f6bc5_GC%20AI%20220px%20(1).png)

Claude의 1M 컨텍스트를 활용하면 사내 변호사가 100페이지짜리 파트너십 계약서의 다섯 차례 협상 라운드를 한 세션에 모두 담아, 협상의 전체 흐름을 비로소 한눈에 파악할 수 있습니다. 더 이상 버전 간을 오가거나 세 라운드 전에 무엇이 바뀌었는지 놓칠 일이 없습니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31397615d221067e19bda_Resolve%20SVG%20original%20color.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b31393431c1a52a589e3a9_Resolve%20SVG%20light%20color.svg)

대규모 프로덕션 시스템에는 끝없는 컨텍스트가 존재하며, 프로덕션 인시던트는 매우 복잡해질 수 있습니다. Claude의 1M 컨텍스트 창 덕분에 모든 엔티티, 시그널, 진행 중인 가설을 최초 알림부터 조치 완료까지 한눈에 유지할 수 있으며, 이러한 시스템의 미묘한 부분을 반복적으로 압축하거나 타협할 필요가 없습니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016becf0259a067d4331fa_logo_hex-light.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69016beff1534c67cafdc9b5_logo_hex-dark.svg)

Opus의 컨텍스트 창을 200k에서 500k로 늘렸더니 에이전트가 더 효율적으로 동작하며, 실제로는 전체 토큰을 더 적게 사용합니다. 오버헤드는 줄고, 당면한 목표에 더 집중하게 됩니다.

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f258769ad971ea1c706eff_endex-light-mode.svg)

![Logo](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69f25878946166279d98b9fb_endex-dark-mode.svg)

실제 스프레드시트 작업에는 깊이 있는 리서치와 복잡한 멀티 스텝 계획이 필요합니다. Claude의 1M 컨텍스트 창은 작업 일관성과 세부 사항에 대한 집중을 유지할 수 있게 해 줍니다.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

### 시작하기

100만 컨텍스트는 현재 Claude Platform 기본 환경, Amazon Bedrock, Google Cloud의 Vertex AI, Microsoft Foundry를 통해 사용 가능합니다. Claude Code Max, Team, Enterprise 사용자는 Opus 4.6에서 자동으로 100만 컨텍스트가 기본 적용됩니다.

자세한 내용은 당사의[문서](https://platform.claude.com/docs/en/build-with-claude/context-windows)와[요금 안내](https://platform.claude.com/docs/en/about-claude/pricing)를 참조하세요.

‍

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

### Claude for Excel 및 Claude for PowerPoint 향상

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

### skill-creator 개선: Agent Skills 테스트, 측정 및 개선

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226da492fb9f7f815ba_1c3d1af62032009538b8bf5864139ca124b06741-1000x1000.svg)

### 엔터프라이즈 전반에서 팀을 위한 Cowork 및 플러그인

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

### 데스크톱용 Claude Code에 자동화된 미리보기, 검토, 병합 기능 도입

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/1m-context-ga
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
