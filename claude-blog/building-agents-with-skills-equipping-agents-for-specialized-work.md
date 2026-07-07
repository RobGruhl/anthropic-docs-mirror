# Skills로 에이전트 구축: 전문 업무를 위한 에이전트 역량 갖추기
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22949f86cd1968deb9f_33dbe8f783d4835a838b4c4ae85d3c04e352fee1-1000x1000.svg)

# Skills로 에이전트 구축: 전문 업무를 위한 에이전트 역량 갖추기

Skills는 에이전트가 접근하고 활용할 수 있는 파일에 업무 전문성을 담아, 범용 에이전트를 실제 업무에 바로 투입 가능한 전문 에이전트로 전환합니다.

- 카테고리에이전트Claude Code

- 제품Claude Code

- 날짜2026-01-22

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work

지난 1년간 많은 변화가 있었습니다. MCP는 업계 리더와 개발자 커뮤니티에서 빠르게 채택되면서 에이전트 연결의 표준으로 자리 잡았습니다.[Claude Code는](https://www.anthropic.com/news/claude-3-7-sonnet)범용 코딩 에이전트로 출시되었습니다. 또한[Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk)를 통해, 이제는 별도의 구성 없이 바로 프로덕션 환경에서 사용할 수 있는 에이전트도 제공합니다.

그러나 이러한 에이전트를 구축하고 배포하면서, 우리는 동일한 간극을 반복적으로 확인했습니다. 에이전트는 지능과 기능을 갖추고 있지만, 실제 업무를 제대로 수행하기 위한 '전문성'은 부족한 경우가 많았습니다. 이 문제를 해결하기 위해[Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)가 탄생했습니다. Skill은 워크플로우, 모범 사례, 스크립트와 같이 업무에 필요한 전문 지식을 에이전트가 접근하여 활용할 수 있는 형태로 정리해 둔 체계적인 파일 모음입니다. 이를 통해 유능한 범용 에이전트를 풍부한 지식을 갖춘 전문 에이전트로 확장할 수 있습니다.

이 게시물에서는 우리가 왜 특화된 에이전트 구축을 중단하고 대신 Skills를 만들기 시작했는지, 그리고 이러한 변화가 에이전트 역량 확장에 대한 우리의 관점을 어떻게 바꾸고 있는지 소개합니다.

## 새로운 패러다임: 이제 필요한 것은 코드뿐입니다

처음에는 업무 영역이 다르면 에이전트도 크게 달라질 것이라고 생각했습니다. 코딩 에이전트, 리서치 에이전트, 재무 에이전트, 마케팅 에이전트 등 각각 고유한 도구와 이를 뒷받침하는 구조가 필요해 보였습니다. 실제로 업계에서도 이러한 분야별 특화 에이전트 모델을 받아들였습니다. 하지만 모델의 지능이 높아지고, 에이전트 역량이 발전하면서, 우리는 점차 다른 접근 방식으로 방향을 바꾸게 되었습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972a852db1883d8c862151f_building-agents-with-skills-fig1-v3%402x.png)

우리는 코드를 더 이상 하나의 활용 사례가 아니라, 에이전트가 거의 모든 디지털 업무를 수행할 수 있게 해주는 인터페이스로 보게 되었습니다. Claude Code는 코딩 에이전트이지만, 코드를 통해 작동하는 범용 에이전트이기도 합니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972a8b8cb336e177c409445_building-agents-with-skills-fig2-v4%402x.png)

Claude Code로 재무 보고서를 작성한다고 생각해 보겠습니다. Claude Code는 리서치를 위해 API를 호출하고, 데이터를 파일 시스템에 저장하며, Python으로 분석하고, 인사이트까지 정리할 수 있습니다. 이 모든 과정은 코드를 통해 이루어집니다. 이 작업을 뒷받침하는 구조는 bash와 파일 시스템 정도로 단순해집니다.

하지만 범용적인 역량이 곧 전문성을 의미하는 것은 아닙니다. 실제 업무에 Claude Code를 사용하기 시작하자, 그 한계가 분명하게 드러났습니다.

## 빠져 있던 마지막 요소: 업무 전문성

세금 신고를 맡겨야 한다면, 원리부터 하나씩 풀어 가는 수학 천재와 수천 건의 신고를 처리해 본 숙련된 세무 전문가 중 누구를 선택하시겠습니까? 대부분의 사람들은 세금 전문가를 선택할 것입니다. 그들이 더 똑똑해서가 아니라, 필요한 전문 지식을 갖추고 있기 때문입니다.

오늘날 에이전트는 그 수학 천재와 비슷합니다. 새로운 상황을 추론하는 능력은 탁월하지만, 숙련된 전문가가 축적한 전문성은 부족한 경우가 많습니다. 적절한 가이드만 주어지만 놀라운 성과를 낼 수 있습니다. 하지만 중요한 맥락이 부족한 경우가 많고, 조직의 전문 지식을 쉽게 흡수하지 못하며, 반복적인 작업을 한다고 해서 자동으로 경험이 누적되지도 않습니다.

Skills는 에이전트가 점진적으로 접근하고 적용할 수 있는 형식으로 업무 전문성을 담아내, 이러한 간극을 해소합니다.

## Agent Skills는 무엇인가요?

Skills는 에이전트가 활용할 수 있도록 업무 전문성과 절차적 지식을 정리해 제공합니다.

```

```

Skills의 단순한 구조는 의도된 것입니다. 파일은 이미 사용 중인 환경에서 그대로 활용할 수 있는 보편적인 단위입니다. Git으로 버전을 관리하고, Google Drive에 저장하며, 팀과 공유할 수 있습니다. 또한 이러한 단순함 덕분에 Skills를 만드는 일은 엔지니어의 영역에만 국한되지 않습니다. 제품 관리자, 분석가뿐 아니라, 각 분야의 전문가들도 이미 자신들의 워크플로우를 체계화하기 위해 Skills를 구축하고 있습니다.

## 점진적 공개

Skills에는 방대한 정보가 포함될 수 있습니다. 하지만 컨텍스트 창을 보호하고 Skills를 함께 조합해 사용할 수 있도록 하기 위해 Skills는 점진적 공개 방식을 따릅니다. 런타임 시, 모델에 제공되는 것은 메타데이터(YAML 프론트매터의 이름과 설명)뿐입니다.

```

```

Claude가 Skill이 필요하다고 판단하면, 전체 SKILL.md 파일을 읽습니다. 더 자세한 정보가 필요한 경우에는, references/ 디렉터리에 보조 문서를 포함할 수 있고, 이 문서들은 필요할 때만 로드됩니다.

이러한 3단계 접근 방식을 통해, 에이전트의 컨텍스트 창에 과부하를 주지 않으면서도, 하나의 에이전트에 수백 개의 Skill을 갖추게 할 수 있습니다. 메타데이터는 약 50토큰, 전체 SKILL.md 파일은 약 500토큰, 참조 파일은 2,000토큰 이상이지만, 실제로 필요할 때만 로드됩니다.

## Skills는 도구처럼 사용할 수 있는 스크립트 포함 가능

기존 도구에는 몇 가지 문제가 있습니다. 설명 문서가 부실하게 작성되어 있는 경우도 있고, 모델이 이를 수정하거나 확장하지 못하는 경우도 있으며, 컨텍스트 창만 불필요하게 늘리는 경우도 많습니다. 반면, 코드는 그 자체로 설명력이 있고, 수정 가능하며, 항상 컨텍스트에 포함되어 있을 필요가 없습니다.

실제 예시를 살펴보겠습니다. 우리는 Claude가 슬라이드에 Anthropic 스타일링을 적용할 때마다, 동일한 스크립트를 반복해서 작성하는 모습을 자주 보게 되었습니다. 그래서 Claude가 그 스크립트를 스스로 사용할 수 있는 도구로 저장하게 했습니다.

```

```

slide-decks.md 문서에서는 이 스크립트를 참조하기만 하면 됩니다.

```

```

## Skills 생태계

Skills 생태계는 빠르게 확장되었으며, 지금까지 크게 3가지 유형의 Skills가 등장했습니다.

### 기본 Skills

이 유형의 Skills는 문서, 스프레드시트, 프레젠테이션처럼 누구에게나 필요한 핵심 기능을 제공합니다. 또한 문서 생성과 편집을 위한 위한 모범 사례도 함께 지원합니다. 실제로 어떻게 적용되는지 알고 싶다면,[Anthropic의 공용 리포지토리에 있는 기본 Skills](https://github.com/anthropics/skills/tree/main/skills/public)를 살펴보세요.

### 파트너 Skills

Skills가 에이전트와 전문 기능 간의 상호작용하는 방식을 표준화하면서, 기업은 자사 서비스가 에이전트를 활용할 수 있도록 Skills를 구축하고 있습니다.[K-Dense](https://github.com/K-Dense-AI/claude-scientific-skills),[Browserbase](https://github.com/browserbase/agent-browse),[Notion](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)등[많은 기업들](https://claude.com/blog/organization-skills-and-directory)은 자사 서비스를 직접 통합하는 Skills를 만들고 있습니다. 이는 Skills 형식의 단순함은 유지하면서, 특정 영역에서 Claude의 역량을 확장하는 것입니다.

### 엔터프라이즈 Skills

조직은 자사의 내부 프로세스와 업무 전문성을 반영한 고유한 Skills를 구축합니다. Skills는 에이전트가 엔터프라이즈 업무에 실질적으로 도움이 되도록, 구체적인 워크플로우, 규정 준수 요건, 그리고 조직 내부의 지식을 포착하는 역할을 합니다.

## 우리가 주목하는 트렌드

Skills 도입이 증가함에 따라, 이 패러다임이 앞으로 어떤 방향으로 발전할지 보여주는 몇 가지 패턴이 나타나고 있습니다. 이러한 흐름은 Skill 설계에 대한 우리의 관점과 Skill 개발자를 지원하기 위해 만들고 있는 도구에도 영향을 주고 있습니다.

### 점차 고도화되는 Skills

초기 Skills는 단순한 문서 참조에 불과했습니다. 이제 여러 도구를 오가며, 데이터 검색, 복잡한 계산, 형식이 지정된 결과물 생성까지 처리하는 정교한 다단계 워크플로우로 발전하고 있습니다.

- 간단한 수준: "서비스 상태 보고서 작성기"(~100줄) - 템플릿 및 서식 지정

- 중간 수준: "재무 모델 빌더"(~800줄) - 데이터 조회, Python을 사용한 Excel 모델링

- 고도화된 수준: "RNA 시퀀싱 파이프라인"(2,500줄 이상) - HISAT2, StringTie, DESeq2 분석 조율

### Skills 및 MCP

[Skills와 MCP 서버는 함께 맞물려 작동합니다](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers). 예를 들어, 경쟁사 분석 Skill은 웹 검색, MCP를 통한 내부 데이터베이스, Slack 메시지 기록, Notion 페이지를 함께 활용해 종합적인 보고서를 작성할 수 있습니다.

### 비개발자로 확장

Skill 생성은 이제 엔지니어의 영역을 넘어, 제품 관리자, 애널리스트, 다양한 분야의 전문가들로 확장되고 있습니다. 이들은 과정을 대화형으로 안내하는 skill-creator 도구를 활용해 30분 내에 첫 번째 Skill을 만들고 테스트할 수 있습니다. 또한 누구나 자신의 전문 지식을 정리하고 공유할 수 있도록, 더 나은 도구와 템플릿으로 Skill 생성 과정을 한층 더 쉽게 만들고 있습니다.

## 전체 아키텍처

지금까지 살펴본 내용을 종합하면, 새롭게 나타나고 있는 에이전트 아키텍처는 다음 요소들이 결합된 형태입니다.

- Agent 루프: 다음 작업을 결정하는 핵심 추론 시스템

- Agent 런타임: 실행 환경(코드, 파일 시스템)

- MCP 서버: 외부 도구 및 데이터 소스와 연결

- Skills 라이브러리: 업무 전문성 및 절차적 지식

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6972ab24ac6df74ad6704f37_building-agents-with-skills-fig3-v2%402x.png)

각 계층의 역할은 명확합니다. 루프는 추론하고, 런타임은 실행하며, MCP는 연결하고, Skills는 안내합니다. 이렇게 분리되어 시스템을 더 쉽게 이해할 수 있고, 각 요소도 독립적으로 발전시킬 수 있습니다.

이 아키텍처에 Skill 하나를 추가할 때 어떤 변화가 일어나는지 살펴보겠습니다.[프론트엔드 디자인 Skill](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design)하나만으로도 Claude의 프론트엔드 역량을 즉시 변화시킵니다. 타이포그래피, 색채 이론, 애니메이션에 대한 전문 가이드를 제공하며, 웹 인터페이스를 구축할 때만 활성화됩니다. 점진적 공개란 관련 있을 때만 로드된다는 것을 의미합니다. 새로운 역량을 추가하는 일은 아주 간단합니다.

## 새로운 산업 영역으로 배포되는 Skills

MCP 서버와 Skills를 갖춘 범용 에이전트라는 이 새로운 패턴은 이미 Claude를 새로운 분야에 배포하는 데 도움이 되고 있습니다.

### 금융 서비스

Skills 출시 직후, 우리는[금융 서비용 Claude](https://www.anthropic.com/news/claude-for-financial-services)를 강화하기 위해, 금융 전문가들에게 더욱 유용한 Skills를 추가했습니다.

- DCF 모델 빌더: 적절한 WACC 계산과 민감도 분석을 통해 DCF(Discounted Cash Flow) 모델을 구축합니다.

- 유사 기업 비교 분석: 관련 멀티플(Multiples)과 벤치마킹을 포함한 comps 테이블 생성

- 실적 분석: 분기별 실적을 처리하여 투자 업데이트 보고서 작성

- 커버리지 개시: 재무 모델이 포함된 종합 리서치 보고서 작성

- 실사: 표준화된 프레임워크로 M&A 분석 구조화

- 피치 자료: 업계 표준에 따라 고객 프레젠테이션 작성

### 헬스케어 및 생명과학

연구자, 임상의, 헬스케어 개발자들이 더 유용하게 활용할 수 있도록 Skills를 통해[헬스케어 및 생명과학 분야용 Claude 서비스](https://www.anthropic.com/news/healthcare-life-sciences)를 강화했습니다.

- 생물정보학 번들: scVI-tools와 Nextflow 배포를 위한 Skills로, 유전체 파이프라인과 단일 세포 RNA 시퀀싱을 관리하는 데 필수

- 임상 시험 프로토콜 생성: 임상 연구를 위한 프로토콜 개발 가속화

- 과학적 문제 선정: 연구자들이 영향력 있는 연구 질문을 식별하고 구체화할 수 있도록 지원

- FHIR 개발: 개발자가 의료 데이터 상호 운용성을 위해 보다 정확하게 코드를 작성하고, 오류를 줄이면서 의료 시스템을 더 빠르게 연계할 수 있도록 지원

- 사전 승인 검토: 보장 요건, 임상 가이드라인, 환자 기록을 교차 검토해 행정적 부담을 줄이고, 환자가 필요한 치료를 더 빨리 받을 수 있도록 지원

## Agent Skills 표준화

이 비전을 실현하기 위해, 우리는[Agent Skills](https://agentskills.io)를 오픈 표준으로 공개하고 있습니다. MCP와 마찬가지로, Skills는 다양한 도구와 플랫폼 간에 자유롭게 사용할 수 있어야 합니다. 동일한 Skill은 Claude나 다른 AI 플랫폼에서도 동일하게 작동해야 합니다. 우리는 이를 위해 생태계의 여러 구성원들과 협력해 이 표준을 구축해 왔으며, 이미 초기 도입이 이루어지고 있습니다.

사용자가 AI 에이전트를 처음 사용하더라도, Skills가 전문성을 담아 전달하기 때문에 에이전트는 사용자와 그 팀이 중요하게 생각하는 것을 이미 파악하고 있습니다. 이 생태계가 성장함에 따라, 커뮤니티의 다른 누군가가 만든 Skill은 어떤 AI 플랫폼을 사용하든 여러분의 에이전트를 더 유용하고, 더 신뢰할 수 있으며, 더 강력하게 만들 수 있습니다.

## 시작하기

우리는 범용 에이전트를 위한 아키텍처로 나아가고 있으며, Skills는 새로운 역량을 배포하고 공유하는 패러다임을 제시합니다. 진정한 가치는 우리가 함께 쌓아가는 집단적 지식 기반에서 만들어집니다. 전문 지식을 포착하고, 이를 팀 사이에 확산시키며, 모든 에이전트가 이전보다 더 뛰어난 역량을 갖출 수 있도록 만드는 것입니다.

리소스:

- 에이전트 대신 Skills를 구축하세요(YouTube 영상)

- Skills 문서

- GitHub 리포지토리

- Skills Cookbook

- Claude에서 Skills 사용

- Skills API 퀵스타트

- Skills 모범 사례 문서

### 감사의 말:

Barry Zhang, Mahesh Murag, Keith Lazuka, Ryan Whitehead

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d225588ad176f7c4aafd_abc884c723daea810d2e986455358281a2f94102-1000x1000.svg)

### Agent Harness Design: 3 Patterns for Harnessing Claude's Intelligence

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22d7d4c10df6024f7bc_ee580919acaba2ddc07425f7a7390c8962cadc94-1000x1000.svg)

### Building agents with the Claude Agent SDK

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

### A Field Guide to Claude Fable: Finding Your Unknowns

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

### AI가 COBOL 현대화의 비용 장벽을 극복하도록 지원하는 방법

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/building-agents-with-skills-equipping-agents-for-specialized-work
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
