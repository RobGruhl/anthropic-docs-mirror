# Claude for Excel 및 Claude for PowerPoint 향상
*May 14, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

# Claude for Excel 및 Claude for PowerPoint 향상

이제 Claude for Excel과 Claude for PowerPoint는 열려 있는 파일 전반에서 전체 컨텍스트를 공유하며, Skills를 통해 어떤 워크플로우든 즉시 반복해 활용할 수 있게 해줍니다.

- 카테고리엔터프라이즈 AI

- 제품Claude Enterprise

- 날짜2026-03-11

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/claude-excel-powerpoint-updates

업데이트:이제 Team 및 Enterprise 플랜에서 Claude for Word 베타를 사용할 수 있습니다. (2026년 4월 10일)

오늘부터[Claude for Excel](https://claude.com/claude-in-excel)및[Claude for PowerPoint](https://claude.com/claude-in-powerpoint)는 열린 모든 파일에서 대화의 전체 컨텍스트를 공유하므로, 애플리케이션 하나에서 Claude가 수행하는 모든 작업은 다른 애플리케이션에서 진행되는 모든 상황을 파악한 상태에서 진행되는 것입니다.

이제 Skill을 Excel 및 PowerPoint 애드인 내에서도 사용할 수 있으며, Claude for Excel과 PowerPoint는 3개의 주요 클라우드 플랫폼인 Amazon Bedrock, Google Cloud의 Vertex AI, Microsoft Foundry를 통해 사용할 수 있습니다.

이러한 업데이트를 통해 Claude는 작업, 스프레드시트, 슬라이드 간에 이동할 수 있으므로, 단계마다 다시 설명하지 않아도 더 높은 효율성과 품질로 작업할 수 있습니다.

## Excel과 PowerPoint 간에 하나의 대화

Claude는 하나의 지속적인 대화에서 여러 Excel 및 PowerPoint 파일 간에 컨텍스트를 전달할 수 있습니다. 셀 값 읽기, 수식 작성, 데이터셋 병합, 슬라이드 편집, 열린 Excel 및 PowerPoint 파일 간에 사용자 대화 전달이 모두 가능합니다.

재무 분석가는 열려 있는 통합 문서와 기타 데이터 소스에서 비교 가능한 회사 재무 데이터를 가져올 수 있습니다. 탭을 전환하거나 각 단계에서 데이터셋을 다시 설명하지 않아도 Excel에서 상대가치비교표를 작성하여 그 평가 요약을 제안서에 삽입한 뒤 MD에게 보낼 이메일 초안을 작성할 수 있습니다. 도구 간에 왔다갔다하는 번거로움을 줄이는 것은 최종 결과물을 더 빠르게 완성하는데 핵심입니다.

## Skill을 사용해 모범 사례를 원클릭 작업으로 전환하기

[Skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude)은 전체 워크플로우를 원클릭 작업으로 전환합니다. 어떤 팀원이 회사의 템플릿을 활용해 분산 분석을 실행하거나 고객 제안서를 작성하는 좋은 방법을 찾은 경우 이를 [Skill](https://support.claude.com/en/articles/12512180-use-skills-in-claude)로 저장하면 이후에 해당 프로세스를 즉시 반복할 수 있습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69b18f278891d8d39110c45e_Claude-Blog-Excel-PPT-3P%20(1).png)

가장 일반적인 Excel 및 PowerPoint 사용 사례를 다루는 미리 로드된 스타터 Skill 세트를 제공해 드립니다. Excel의 경우 스타터 Skill은 재무 분석에서 가장 자주 발생하는 워크플로우를 다룹니다:

- 모델의 수식 오류와 대차대조표 무결성 감사

- LBO, DCF, 3대 재무제표 모델 템플릿 구축 및 데이터 입력

- 비교 가능한 회사 분석 실행

- 범위, 활성 시트 또는 전체 파일에서 지저분한 스프레드시트 데이터 정리

PowerPoint의 경우 스타터 Skill은 분석 후에 이어지는 프레젠테이션 레이어 작업을 다룹니다.

- 시장 포지셔닝 및 경쟁사 심층 조사를 포함한 경쟁 환경 보고서 작성

- 새로운 정보나 추가 데이터로 기존 제안서 업데이트

- 투자은행 제안서의 숫자 일관성, 데이터와 서술 간의 정합성, 언어 다듬기 검토

개인 또는 조직 전반에 걸쳐 데스크톱이나 웹 앱을 통해 Claude에 이미 설정된 모든 Skill은 MCP 커넥터와 같은 방식으로 즉시 애드인 내에서 작동합니다. Excel과 PowerPoint의 스타터 Skill은[Financial Analysis 플러그인](https://github.com/anthropics/financial-services-plugins/tree/main/financial-analysis/skills)을 통해서도 사용할 수 있으며, 이 플러그인은 두 애드인 모두에 자동으로 설치됩니다. 플러그인에 추가된 새로운 Skill은 추가 설정 없이도 사용할 수 있습니다.

마지막으로,[지침](https://support.claude.com/en/articles/12512180-use-skills-in-claude)은 항상 적용해야 하는 지속적인 앱 수준 환경 설정을 처리합니다. 여기에는 Excel에서 항상 회사의 숫자 서식을 사용하고, PowerPoint 글머리 기호를 한 줄로 유지하며, 하드코딩된 가정을 참조하는 셀에 플래그를 지정하는 것이 포함될 수 있습니다. [지침](https://support.claude.com/en/articles/12512180-use-skills-in-claude)은 한 번 설정하면 추가 프롬프트 없이 자동으로 적용할 수 있습니다. 또한 Claude는 [지침](https://support.claude.com/en/articles/12512180-use-skills-in-claude)을 작성하고 편집하는 데 도움을 줄 수 있습니다.

## 배포 유연성

Claude for Excel 및 Claude for PowerPoint는 이제 고객이 규정 준수 체계를 이미 구축한 환경에서 그대로 사용할 수 있습니다. 조직은 Claude 계정으로 두 애드인에 액세스하거나, 기존 LLM 게이트웨이를 통해 Amazon Bedrock, Google Cloud의 Vertex AI, Microsoft Foundry에서 실행되는 Claude 모델로 트래픽을 라우팅할 수 있습니다. LLM 게이트웨이와 함께 Claude for Excel과 Claude for PowerPoint 사용에 대한[가이드](https://support.claude.com/en/articles/13945233-use-claude-in-excel-and-powerpoint-with-an-llm-gateway)를 참조하세요.

또한 Claude는[Excel 내에서 기본적으로 에이전트 모드](https://support.microsoft.com/en-gb/topic/use-claude-with-agent-mode-in-excel-b2c3b3ec-154b-484b-84d0-914a80df395a)를 구동하므로, Microsoft 365 Copilot 고객은 Copilot과 함께 엑셀 파일 전체 구조를 작성, 편집, 분석할 수 있습니다.

## 시작하기

유료 플랜을 이용하는 모든 Mac 및 Windows 사용자는 베타 버전에서 제공되는[Claude for Excel](https://claude.com/claude-in-excel)([[가이드 참조](https://support.claude.com/en/articles/13521390-use-claude-in-powerpoint)](https://support.claude.com/en/articles/12650343-use-claude-for-excel))과[Claude for PowerPoint](https://claude.com/claude-in-powerpoint)([[가이드 참조](https://support.claude.com/en/articles/13521390-use-claude-in-powerpoint)](https://support.claude.com/en/articles/12650343-use-claude-for-excel)) 간의 향상된 커뮤니케이션을 경험해 볼 수 있습니다. Excel과 PowerPoint의 Skill은 모든 유료 플랜에서도 사용할 수 있습니다. 이러한 새로운 도구를 최대한 활용하는 모범 사례를 살펴보려면[Claude 웨비나](https://www.anthropic.com/webinars/best-practices-for-claude-in-excel-and-powerpoint)에 등록하세요.

Claude는 Microsoft와의 파트너십을 자랑스럽게 생각하며 더 많은 사람들이 Microsoft 365와 Claude의 힘을 함께 경험할 수 있도록 돕고자 합니다.

‍

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### How Claude Code works in large codebases: Best practices and where to start

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226da492fb9f7f815ba_1c3d1af62032009538b8bf5864139ca124b06741-1000x1000.svg)

### 엔터프라이즈 전반에서 팀을 위한 Cowork 및 플러그인

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d226ca443e2e05990c00_83d7d2fe412ceb4dfe627f0d5f3d64aff1a3f5db-1000x1000.svg)

### Claude Enterprise, 이제 셀프 서비스 방식으로 도입 가능

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/claude-excel-powerpoint-updates
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
