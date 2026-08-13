# Claude를 더 유능한 전기 엔지니어로 만들기
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2222403b092e0358b0e_cd4fd51deacd067d4e30aee4f4b149f6cba1b97b-1000x1000.svg)

# Claude를 더 유능한 전기 엔지니어로 만들기

맞춤형 회로 기판 제조업체와 같은 분야별 전문가와의 협업이 Claude가 전문 분야의 작업을 더 효과적으로 처리하도록 학습하는 데 어떤 도움이 되는지 살펴봅니다.

- 카테고리엔터프라이즈 AI

- 제품Claude Enterprise

- 날짜2025-12-12

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/making-claude-a-better-electrical-engineer

[Diode Computers](https://www.diode.computer/)는 AI를 활용해 맞춤형 회로기판을 설계하고 제조합니다. Diode의 툴체인은 회로기판 설계를 하나의 소프트웨어 문제로 전환합니다. 소프트웨어 엔지니어가 Claude Code와 같은 도구로 효율성을 높일 수 있는 것처럼, Diode 역시 동일한 접근 방식을 적용해 전기 엔지니어가 몇 시간 만에 제조 준비가 완료된 기판을 설계할 수 있도록 지원하고 있습니다.

Diode는 인쇄회로기판(PCB) 회로도를 기술하기 위해[Starlark](https://github.com/diodeinc/[pcb](https://github.com/diodeinc/pcb?tab=readme-ov-file)/blob/main/docs/pages/spec.mdx)기반으로 구축된 도메인 특화 언어인[Zener 언어](https://github.com/bazelbuild/starlark), 그리고 [Zener 언어](https://github.com/bazelbuild/starlark)를 사용해 KiCad 위에서 자동화 기능을 제공하는[pcb](https://github.com/diodeinc/pcb?tab=readme-ov-file)를 개발하고 유지 관리합니다.

전기 엔지니어의 중요한 과제 중 하나는 레퍼런스 디자인을 구축하는 것입니다. 설계자가 특정 칩을 사용하려면, 그 칩이 작동하는 데 필요한 부품이 무엇인지 파악하기 위해 수백 페이지의 문서를 검토해야 합니다. 일반적인 칩 하나에도 저항, 커패시터, 인덕터와 같은 최대 12개의 보조 부품이 필요할 수 있지만, 이를 어떻게 배선해야 하는지에 대한 체계적인 정보는 부족한 경우가 많습니다.

전기 엔지니어들은 이미 검토 전에 Claude Code를활용해, 비정형 문서에서 Zener용 레퍼런스 디자인을 자동 생성하고 있습니다. 그러나 이 환경은 전문 분야에 특화된 도구를 포함하고 있으며, 높은 수준의 전문성을 요구하는 새로운 영역이기 때문에, 레퍼런스 디자인 생성 작업에서 Claude의 에이전틱 성능과 이 특정 전기 엔지니어링 작업에 대한 전반적인 이해는 더 개선될 여지가 있습니다. 레퍼런스 디자인 자동 생성 작업에서 일반적으로 나타나는 실패 사례는 다음과 같습니다.

- 회로 구성 방식에 대한 데이터시트의 세부 사항 누락

- 레퍼런스 회로도 이미지의 잘못된 해석

- Zener에 대한 이해 부족이나 잘못된 사용

심층적인 주제 전문 지식이 필요한 전문 분야 작업에서 Claude의 역량에 부족한 부분이 발견되면, 우리는 해당 분야의 전문가와 협력하여 Claude가 이러한 과제를 더 잘 수행하도록 학습시킬 수 있습니다. 이러한 지식은 공개 출시되는 Claude 모델에 인코딩되므로, Claude Code,[Claude.ai](http://claude.ai)또는 자체 Claude 기반 시스템과 애플리케이션 등 Claude 모델의 모든 사용자가 그 혜택을 받을 수 있습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/693b774140c56c41b9aa9611_image1.png)

## 문제 범위 정의

우리는 Diode와 협력하여, 레퍼런스 디자인을 자동 생성하는 Claude의 역량을 이해하고 개선하기 위한 공동 이니셔티브를 진행했습니다. 이 에이전틱 작업에서 Claude는 칩 관련 문서를 입력으로 받아, 해당 칩의 전체 레퍼런스 디자인을 Zener로 생성해야 합니다. 이를 올바르게 수행하려면 Claude가 수많은 페이지의 문서를 읽고, 밀도 높은 기술 문서와 도표를 이해하며, 칩의 모든 구성과 동작 모드를 완벽하게 반영하는 구성 가능한 회로도를 작성해야 합니다. 이 에이전틱 설정에서, Claude는 파일을 읽거나 쓰고, bash 명령을 실행하는 도구를 제공받습니다. 또한 Zener 컴파일러와 언어 문서, 그리고 일부 예제에만 접근할 수 있으며, 그 외의 정보는 제공되지 않습니다.

레퍼런스 디자인이 올바른지 판단하는 것도 간단한 일이 아닙니다. 문서에는 동작에 필요한 정확한 부품이나 파라미터는 충분히 명시되지 않는 경우가 많습니다. 이 문제를 해결하기 위해, 각 레퍼런스 디자인은 맞춤형테스트벤치를 통해 평가됩니다. 테스트벤치는 개별 부품의 존재를 절대적인 기준으로 검증하기 보다(예: '전원과 접지 사이의 20uF 커패시터'), 더 높은 수준의 요구 사항(예: '전원과 접지 사이에 최소 22uF 이상의 커패시턴스')을 인코딩합니다. 이를 통해 모델이 받는 신호가 정확하면서도 지나치게 제한되지 않게 합니다.

이 과제는 범위가 명확하게 정의되어 있고, 성공과 실패의 판단 기준도 분명했습니다. 우리는 Diode와 협력해 Sonnet 4.5와 이후 Claude 모델의 학습 과정에 개선 사항을 반영하여, 회로기판의 레퍼런스 디자인을 더 효과적으로 자동 생성할 수 있도록 했습니다.

## 결과 벤치마킹

이 작업에서 Claude의 성능을 벤치마킹하기 위해, 우리는 생성된 레퍼런스 디자인의 테스트 세트를 사용하여 Claude Opus 4.1, Claude Sonnet 4, Claude Sonnet 4.5를 블라인드 일대일 비교 방식으로 평가했습니다. 그 결과, Diode의 전기 엔지니어들은 Claude Sonnet 4.5의 레퍼런스 디자인을 10회 중 8회 선호하는 것으로 나타났습니다. 다른 모델과 비교해 Claude Sonnet 4.5는 문서 자료에 담긴 미세한 뉘앙스를 더 잘 포착했고, Diode의 툴체인 관례와 의미 체계를 더 정확하게 따랐습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/693b7d9fc08424b878617a4a_image2.png)

## 향후 방향

Diode와의 파트너십은 명확한 성공 및 실패 기준이 있는 작업에 Claude가 에이전트 기반 방식으로 적용되는 모든 분야와 산업의 기업으로 확장할 수 있습니다. Anthropic은 Claude를 가능한 한 넓은 분야와 산업에서 최고의 가상 협업자가 될 수 있도록 지속적으로 개선하고 있습니다. 심층적인 주제 전문 지식이 필요하고, 전문 분야에 특화된 프로세스와 도구, 워크플로우를 수반하는 작업과 업무 흐름은 Anthropic과의 보다 긴밀한 협업에 적합합니다.

Claude의 향후 버전을 개선하기 위해 Anthropic과 파트너십에 관심이 있으시다면,[이 양식](https://docs.google.com/forms/d/e/1FAIpQLScs9kVDB_PRyXPueayJ0c4pKUGwFdDwrKlRPsniVXCqw0utQQ/viewform?usp=dialog)을 작성해 주세요. 이후 Anthropic 팀이 연락드리겠습니다.

## 감사의 말

이 글은 Diode Computers의 Davide Asnaghi, Lenny Khazan, Anthropic의 Connor Jennings, David Hershey, Nicholas Marwell이 함께 작성했습니다.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22f06154e381e9a1203_fb2273e9cacb0299a3ee1bf1d76d0bff95ba4e15-1000x1000.svg)

### Anthropic의 그로스 마케팅 팀이 Claude Code를 사용해 광고 제작 시간을 30분에서 30초로 단축한 방법

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d223de65e7dcca8267d8_ea364001be6bf6d2e86b58109ead6a779d5771a7-1000x1000.svg)

### Anthropic 팀의 Claude Code 사용법

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2319ef2161fcf9ba649_ddad92700787ec1bf1d80359c0c5e6ca305682b0-1000x1000.svg)

### Claude for Excel 및 Claude for PowerPoint 향상

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/making-claude-a-better-electrical-engineer
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
