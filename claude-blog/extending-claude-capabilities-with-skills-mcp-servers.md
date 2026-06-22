# Skills MCP 서버로 Claude의 역량 확장
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22b1ef956a6d81cfd9c_653e7474811cf768b6b0f628e253f98c60e2747e-1000x1000.svg)

# Skills MCP 서버로 Claude의 역량 확장

Skill과 MCP가 함께 작동해 워크플로우를 따르고 외부 시스템과 플랫폼을 효과적으로 사용하는 에이전트를 빌드하는 방법을 알아보세요.

- 카테고리에이전트

- 제품Claude 앱Claude Platform

- 날짜2025-12-19

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers

업데이트:플랫폼 간 이식성을 위해[Agent Skills](https://agentskills.io)를개방형 표준으로 공개했습니다. (2025년 12월 18일)[Skills를 출시](https://claude.com/blog/skills)한 이후 고객으로부터 가장 많이 받은 두 가지 질문은 다음과 같습니다. "Skills와 MCP는 어떻게 상호 작용하나요? 언제 다른 하나 대신 하나를 사용해야 하나요?"

[MCP(모델 컨텍스트 프로토콜)](https://modelcontextprotocol.io/docs/getting-started/intro)는 Claude를 타사 도구와 연결하며, Skills는 Claude에 Skills를 잘 사용하는 방법을 가르칩니다. 이 두 가지를 결합하면 지속적인 수정이 필요한 일반적인 프로세스가 아니라 팀의 워크플로우를 따르는 에이전트를 구축할 수 있습니다.

예를 들어, MCP를 통해 Notion에 연결하면 Claude가 사용자의 워크스페이스를 검색할 수 있습니다. 회의 준비를 위한 Skill을 추가하면, Claude는어떤페이지에서 가져올지, 준비 문서를어떻게형식화할지, 회의 메모를 전달하기 위한 팀의 표준이무엇인지알게 됩니다. 이러한 연결은 단순히 사용할 수 있는 것을 뛰어넘어 유용하게 됩니다.

이 문서에서는 Skills와 MCP 간의 관계를 분석하고, 워크플로우에 따라 일관된 결과물을 생성하는 에이전트를 구축하기 위해 이를 어떻게 결합할 수 있는지, 그리고 실제로 어떻게 함께 작동하는지에 대한 몇 가지 실제 사례를 살펴보겠습니다.

## Skills와 MCP 이해

망가진 캐비닛을 고치려고 하드웨어 매장을 방문합니다. 매장에는 필요한 모든 것(목제 접착제, 클램프, 교체용 힌지)이 갖춰져 있지만, 어떤 물건을 구매해야 하는지, 어떻게 사용하는지 아는 것은 다른 문제입니다.

MCP는 매장의 통로에 다가가는 것과 같습니다. 한편 Skills는 직원의 전문 지식과 같습니다. 어떤 항목이 필요한지 혹은 항목을 어떻게 사용해야 할지 모른다면 전 세계의 모든 인벤토리는 무용지물입니다. Skill은 수리 프로세스를 안내하고, 올바른 용품을 안내하며, 적절한 기법을 보여주며 도움을 주는 직원과 같습니다.

더 구체적으로 설명하면, MCP 서버는 Claude에게 외부 시스템, 서비스, 플랫폼에 대한 액세스 권한을 제공하고, Skills는 Claude가 이러한 연결을 효과적으로 활용하는 데 필요한 컨텍스트를 제공하며, 이 액세스 권한이 있으면 Claude가 무엇을 해야 하는지 가르쳐줍니다.Skills가 제공하는 컨텍스트가 없으면 Claude는 사용자가 원하는 내용을 추측해야 합니다. Skills을 사용하면 Claude가 사용자의 플레이북을 대신 따라 수행할 수 있습니다.

## Skills와 MCP가 함께 잘 작동하는 이유

MCP는 외부 시스템에 대한 안전하고 표준화된 액세스인 연결성을 처리합니다. GitHub, Salesforce, Notion 또는 자체 내부 API에 연결하든, MCP 서버는 Claude가 도구와 데이터에 접근할 수 있는 기능을 제공합니다.

Skills는 원시 도구 액세스를 신뢰할 수 있는 결과로 전환하는 도메인 지식과 워크플로우 로직인 전문성을 처리합니다. Skills는 CRM을 언제 쿼리해야 하고, 결과에서 무엇을 찾아야 하며, 출력 형식을 어떻게 지정해야 하는지, 어떤 에지 사례에 다른 처리가 필요한지를 알고 있습니다.이러한 분리는 아키텍처를 구성 가능하게 유지합니다. 단일 Skill이 여러 MCP 서버를 조정할 수 있으며, 단일 MCP 서버는 수십 개의 서로 다른 Skill을 지원할 수 있습니다. 새로운 연결을 추가하면 기존 Skill이 새 연결을 통합할 수 있습니다. Skills을 다듬으면 연결된 모든 도구에서 작동합니다.

#### Skills와 MCP를 결합하면 다음과 같은 이점을 얻을 수 있습니다.

명확한 발견: Claude는 어디를 찾아야 할지 더 이상 추측하지 않습니다. 회의 준비 Skill은 먼저 프로젝트 페이지를 확인하고 이전 회의 메모를 확인한 다음 이해관계자 프로필을 확인하도록 지정할 수 있습니다. 리서치 Skills은 공유 드라이브로 시작하고, CRM과 상호 참조한 다음, 웹 검색으로 빈 부분을 메우라고 지정할 수 있습니다. 이 Skill은 어떤 작업에 어떤 소스가 중요한지에 대한 조직의 지식을 담고 있습니다.

안정적인 오케스트레이션: 다단계 워크플로우가 예측 가능하게 됩니다. Skill이 없으면 Claude는 모든 것이 포함되어 있는지 확인하기 전에 데이터를 가져와 서식을 지정할 수도 있습니다. Skills는 시퀀스를 명시적으로 정의하므로, Claude 매번 동일한 방식으로 워크플로우를 실행합니다.

일관된 성능: 결과물이 실제로 표준을 충족합니다. 일반적인 결과에는 편집이 필요합니다. Skills는 팀을 위해 적합한 구조, 올바른 세부 정보 수준, 청중에게 적합한 어조 등 '완료'란 어떤 상태인지 정의합니다.

시간이 지남에 따라 팀이 상호 연관된 Skills과 연결을 쌓아가면 Claude가 특정 도메인에서 전문성을 갖출 수 있게 됩니다.

추가 자료: Tim O'Reilly의[오픈 소스 AI에서 MCP와 Skills가 의미하는 바](https://www.oreilly.com/radar/what-mcp-and-claude-skills-teach-us-about-open-source-for-ai/)

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6945b3dfa8f134d0104e4e23_How%20Skills%20and%20MCP%20work%20together%20-%20v3B%402x%20(2).png)

#### Skills와 MCP가 겹칠 수 있는 부분

MCP 서버에는 일반적인 작업에 대한 도구 사용 힌트와 프롬프트 형식의 지침이 포함될 수 있습니다. 이를 통해 도구별 지식을 도구에 가까이 유지할 수 있습니다. 그러나 이러한 지침은 설계상 일반적이어야 합니다.

기본 원칙: MCP 지침은 서버와 도구를 올바르게 사용하는 방법을 설명합니다. Skill 지침은 지정된 프로세스나 멀티서버 워크플로우에서 Skill을 사용하는 방법을 설명합니다.

예를 들어, Salesforce MCP 서버는 쿼리 구문과 API 형식을 지정할 수 있습니다. Skill은 먼저 확인할 기록을 지정하고 최근 컨텍스트를 위해 Slack 대화와 상호 참조하는 방법과 팀의 파이프라인 검토를 위해 결과물을 구성하는 방법을 지정합니다.MCP 서버와 Skills를 조합할 때 지침이 충돌하지 않는지 확인하세요. MCP 서버가 JSON을 반환하라고 지시하고 Skill이 마크다운 테이블로 형식을 지정하라고 지시하면, Claude는 어느 지침이 옳은지 추측해야 합니다. MCP가 연결성을 처리하게 하고 Skills가 표시, 시퀀싱, 워크플로우 로직을 처리하게 하세요.

추가 자료:Skills가[점진적 공개](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)를 활용해 온디맨드로 컨텍스트를 로드하고,[프로그래밍 방식 도구 호출](https://www.anthropic.com/engineering/advanced-tool-use)을 활용해 MCP 도구를 효율적으로 조정하는 방법을 알아보세요.

## Skills와 MCP를 함께 사용한 실제 사례

이제 실제 워크플로우에서 Skills와 MCP가 어떻게 결합되는지 살펴보겠습니다. 다음 두 가지 사례를 살펴보겠습니다. 회사 평가를 위해 실시간 시장 데이터를 가져오는 재무 분석가와 회의 준비를 위해 Notion의 회의 인텔리전스 Skill을 사용하는 프로젝트 관리자입니다.

두 경우 모두 MCP 서버는 도구에 대한 액세스를 제공하고 Skills는 도구로 할 일을 정의합니다.

#### 재무 분석: 회사 평가 자동화 Skill

Anthropic은 유사 기업 분석을 포함해 일반적인 재무 워크플로우를 위한[사전 빌드된 Skill 세트를 출시했습니다](https://www.anthropic.com/news/advancing-claude-for-financial-services). 유사 기업 분석은 표준 평가 방법입니다. 유사 기업 분석을 수행하는 분석가는 몇 시간을 들여 여러 소스에서 재무 지표를 가져오고, 동일한 평가 방법론을 적용하며, 규정 준수 표준을 충족하도록 결과물의 형식을 지정합니다. 이는 반복적이고 오류가 발생하기 쉬우며, Skills와 MCP가 함께 작동할 때 정확히 이점을 얻는 종류의 워크플로우입니다.

Skill:[유사 기업 분석](https://www.anthropic.com/news/advancing-claude-for-financial-services)은 이 평가 워크플로우를 자동화하고 여러 소스에서 데이터를 가져오며, 일관된 방법론을 적용하고, 결과물을 특정 표준에 맞게 형식을 지정합니다.

MCP 서버: 실시간 시장 데이터를 얻기 위한 S&P Capital IQ, Daloopa, Morningstar에 대한 연결

워크플로우:

- Skills는 쿼리할 데이터 소스를 식별합니다(발견).

- MCP 연결은 실시간 재무 데이터를 가져옵니다

- Skill은 방법론을 적용하고 출력 형식을 지정합니다(오케스트레이션).

- Skill은 규정 준수 요구 사항에 따라 검증합니다(수행).

#### 회의 준비: Notion의 회의 인텔리전스 Skill

회의 준비는 지루한 작업입니다. 프로젝트 문서, 이전 회의 메모, 이해관계자 정보 등 여러 곳에서 컨텍스트를 가져온 다음, 미리 읽을 자료와 의제로 종합해 정리해야 합니다. 매번 다시 설명하게 되는 여러 단계로 구성된 프로세스입니다.

Skill:[회의 인텔리전스](https://notiondevs.notion.site/notion-skills-for-claude)는 검색할 페이지, 결과물을 구성하는 방법, 포함할 섹션을 정의합니다.

MCP 서버: 페이지를 검색, 읽기, 생성하는 Notion 연결

워크플로우:

- Skill은 프로젝트, 이전 회의, 이해관계자 정보 등 검색할 관련 페이지를 식별합니다(발견).

- MCP 연결은 Notion에서 콘텐츠를 검색하고 가져옵니다.

- Skill은 내부 사전 검토 자료 및 외부 의제의 두 문서를 구성합니다(오케스트레이션).

- MCP 연결을 통해 두 문서가 Notion에 저장되면 내용이 정리되고 연결됩니다.

- Skill은 결과물이 서식 표준에 부합하도록 보장합니다(수행).

## Skills과 MCP를 각각 사용해야 할 때

Skills와 MCP는 서로 다른 문제를 해결하지만, 특정 워크플로우에 어떤 것을 사용할지 항상 명확하게 결정되는 것은 아닙니다.

#### Skills를 사용하는 목적

Skills는 머리 속에만 남아 있는 지식이나 새로운 인원이 팀에 합류할 때마다 다시 설명해야 하는 지식을 캡처합니다. Skills는 다음과 같은 경우에 가장 적합합니다.

- 도구가 포함된 다단계 워크플로우: 여러 소스에서 가져온 다음 구조화된 문서를 생성하는 회의 준비

- 일관성이 중요한 프로세스: 매번 동일한 방법론을 반드시 따라야 하는 분기별 재무 분석, 필수 체크포인트가 포함된 규정 준수 검토

- 캡처 및 공유하려는 분야 전문성: 리서치 방법론, 코드 검토 표준, 작성 가이드라인

- 팀원이 퇴사하더라도 유지해야 하는 워크플로우: 재사용 가능한 지침으로 인코딩된 조직 내 지식

#### MCP 서버를 사용하는 목적

MCP는 Claude가 접근하고 사용할 수 있는 내용을 확장합니다. MCP는 다음과 같은 필요에 따라 사용합니다.

- 실시간 데이터 액세스: Notion 페이지 검색, Slack 메시지 읽기, 데이터베이스 쿼리

- 외부 시스템에서 작업: GitHub 이슈 생성, 프로젝트 관리 도구 업데이트, 알림 전송

- 파일 작업: Google Drive에서 읽기 및 쓰기, 로컬 파일 시스템에 액세스

- API 통합: 기본 Claude 지원이 없는 서비스에 연결

무언가를 수행하는방법을 설명하고 있다면 그것은 Skill입니다. Claude가 무언가에액세스해야 한다면 그것은 바로 MCP입니다.

‍

#### 빠른 참조표: Skills와 MCP의 차이점

## 일반적인 질문

#### Skills가 MCP를 대체하나요?

아니요. Skills는 MCP는 다른 문제를 해결합니다. MCP는 외부 도구와 데이터에 대한 연결을 제공합니다. Skills는 해당 연결성을 효과적으로 활용하는 방법에 대한 절차 지식을 제공합니다. 대부분의 강력한 워크플로우에서는 둘 다 사용합니다.

#### 하나의 Skill이 MCP 서버를 여러 개 사용할 수 있나요?

네, 단일 Skill이 여러 MCP 서버를 한 번에 조정할 수 있습니다. 기술 경쟁 분석 Skill은 Google Drive에서 내부 리서치를 검색하고, GitHub에서 경쟁사 리포지토리를 가져오며, 웹 검색을 통해 시장 데이터를 수집할 수 있습니다.

#### MCP 서버 하나에 Skill을 여러 개 빌드할 수 있나요?

네, Skill은 단일 MCP 연결에서 얻는 가치를 높일 수 있습니다. Notion은 회의 준비, 리서치, 지식 캡처, 사양에서 구현으로의 전환을 위한 별도의 Skill로 이 패턴을 입증합니다.[여기](https://claude.com/connectors/notion)에서 확인하세요.

## 시작하기

Skill과MCP를 사용해 빌드할 준비가 되셨나요? 시작하는 방법은 다음과 같습니다.

Skill 사용 시:

- Claude.ai의 설정 → 기능에서 Skill 활성화

- 사전 빌드된 예시를 살펴보려면Skills 라이브러리둘러보기

- Skills 문서읽기

MCP 사용 시:

- 도구에 맞는MCP 서버찾아보기

- MCP 문서읽기

- MCP 빠른 시작으로 나만의 서버 빌드

둘 다 사용 시:

- MCP 서버를 연결한 후 이 서버를 사용하는 Skill을 추가합니다.

## 관련 문서

Claude의 에이전틱 기능을 사용하여 빌드에 대한 더 많은 인사이트를 살펴보세요.

- Skills 설명: Skills와 프롬프트, 프로젝트, MCP, 서브 에이전트의 차이

- Skills를 통한 프론트엔드 디자인 개선

- 에이전트 스킬(Agent Skills), 실제 환경에 바로 활용할 수 있는 에이전트

‍

‍

‍

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2260bfc90348429f9c3_cd9cf56a7f049285b7c1c8786c0a600cf3d7f317-1000x1000.svg)

### AI 에이전트의 일반적인 워크플로우 패턴과 사용 시점

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226da492fb9f7f815ba_1c3d1af62032009538b8bf5864139ca124b06741-1000x1000.svg)

### 엔터프라이즈 전반에서 팀을 위한 Cowork 및 플러그인

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d230e0a787df988a8558_97cf99624aa60f59b75f9e08cdf0f00d33c34804-1000x1000.svg)

### 멀티 에이전트 시스템 구축: 사용해야 할 시점 및 사용 방법

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22949f86cd1968deb9f_33dbe8f783d4835a838b4c4ae85d3c04e352fee1-1000x1000.svg)

### Skills로 에이전트 구축: 전문 업무를 위한 에이전트 역량 갖추기

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/extending-claude-capabilities-with-skills-mcp-servers
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
