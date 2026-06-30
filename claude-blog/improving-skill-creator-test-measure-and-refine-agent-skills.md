# skill-creator 개선: Agent Skills 테스트, 측정 및 개선
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

# skill-creator 개선: Agent Skills 테스트, 측정 및 개선

이제 Skill 작성자는 Skill이 작동하는지 검증하고, 회귀를 포착하며, 설명을 개선할 수 있습니다.

- 카테고리Claude Code제품 발표

- 제품Claude Code

- 날짜2026-03-03

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills

이제 skill-creator는 평가를 작성하고, 벤치마크를 실행하며,모델이 진화함에 따라 Skill이 계속 작동하도록 지원합니다. 이 업데이트는 이제 Claude.ai와 Cowork에서 제공되며[Claude 리포지토리 내에서](https://github.com/anthropics/skills/tree/main/skills/skill-creator)[Claude Code용 플러그인으로](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator)사용할 수 있습니다.

지난 10월[Agent Skills 출시](https://claude.com/blog/skills)이후 대부분의 작성자는 엔지니어가 아니라 해당 분야의 전문가라는 사실을 확인했습니다. 이들은 워크플로우를 알고 있지만, Skill이 새 모델에서 여전히 작동하는지, 필요할 때 트리거되는지, 편집 후 실제로 개선되었는지 여부를 확인할 수 있는 도구가 없습니다.

오늘 작성자가 더 확신을 가지고 빌드하도록 돕는 skill-creator 향상 기능을 발표합니다. Claude는 누구에게도 코드 작성을 요구하지 않으면서 소프트웨어 개발의 엄격함(테스트, 벤치마킹, 반복 개선)을 skill 작성에 적용하고 있습니다.

## 두 가지 종류의 Skill

Skill은 일반적으로 두 가지 카테고리로 나뉩니다.

역량 향상Skill은 기본 모델이 할 수 없거나 일관되게 진행할 수 없는 작업을 Claude가 수행하도록 도와줍니다.[문서 생성 Skill](https://github.com/anthropics/skills/tree/main/skills)좋은 예시입니다. 이러한 Skill은 프롬프트만 사용하는 것보다 더 나은 결과물을 생성하는 기법과 패턴을 인코딩합니다.

인코딩된 선호도Skill은 Claude가 이미 각 부분을 수행할 수 있는 워크플로우를 문서화해 팀의 프로세스에 따라 순서대로 배열합니다. 예시: 설정된 기준에 따라 NDA 검토를 진행하는 Skill 또는 다양한 MCP의 데이터로 주간 업데이트 초안을 작성하는 Skill.

이 두 가지 유형의 Skill은 서로 다른 이유로 테스트가 필요할 수 있기 때문에 이 구분은 중요합니다.

- 모델이 향상됨에 따라 역량 향상 스킬은 필요성이 떨어질 수 있습니다. 평가는 이러한 상황이 언제 발생했는지 알려줍니다.

- 인코딩된 선호도 skill은 지속성이 뛰어나지만 실제 워크플로우를 얼마나 충실하게 반영하는지에 따라 가치가 달라집니다. 평가는 이러한 충실도를 검증합니다.

어느 쪽이든, 테스트를 통해 작동하는 것처럼보이는skill을확실히작동하는 skill로 전환할 수 있습니다.

## 평가를 활용해 skill 테스트 및 개선

이제 skill-creator는 주어진 프롬프트에서 Claude가 기대하는 대로 수행하는지 확인하는 테스트인 평가 작성을 지원합니다. 소프트웨어 테스트를 작성해 본 적이 있다면 익숙하게 느껴질 것입니다. 몇 가지 테스트 프롬프트(필요한 경우 파일 포함)를 정의하고, 좋은 결과가 어떤 것인지 설명하면, skill-creator가 skill이 제대로 작동하는지 여부를 알려줍니다.

예를 들어, PDF skill은 이전에 작성할 수 없는 양식을 처리하는 데 어려움을 겪고 있었습니다. Claude는 안내해줄 정의된 필드가 없는 상태에서 정확한 좌표에 텍스트를 배치해야 했습니다. 평가를 통해 실패를 격리했고 추출된 텍스트 좌표에 위치를 고정시키는 수정 사항을 배포했습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a237b02128b691d9e8b2af_skillscreator-PDFevals-1920x840-v1.png)

평가는 여러 가지 방법으로 유용하지만 두 가지 중요한 용도는 품질 회귀를 포착하고 모델 진행 상황을 파악하는 것입니다.

첫째,품질 회귀 포착.모델과 이를 둘러싼 인프라가 진화함에 따라 지난 달에 잘 작동했던 기능이 오늘은 다르게 동작할 수 있습니다. 새로운 모델에 대해 평가를 실행하면 무언가 변화가 발생하면 팀의 작업에 영향을 미치기 전에 조기 신호를 얻을 수 있습니다.

둘째,일반적인 모델 역량이 작성한 skill을 넘어서는 시점을 파악하는 것입니다.이는 주로 역량 향상 skill에 적용됩니다. skill이 로드되지않은상태에서 기본 모델이 평가를 통과하기 시작하면 이는 skill의 기법이 모델의 기본 동작에 통합되었을 수 있음을 나타냅니다. skill이 손상된 것이 아니라, 단지 더 이상 필요하지 않을 뿐입니다.

또한 사용자의 평가를 활용해 표준화된 평가를 실행하는벤치마크 모드를 추가했습니다. 이는 모델 업데이트 후 또는 skill 자체를 반복적으로 개선할 때 실행할 수 있는 모드입니다. 평가 통과율, 경과 시간, 토큰 사용량을 추적합니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a237f15fbc61e1ccd00a0a_skillscreator-benchmarkmode-1920x1080-v1.png)

작성한 평가와 평가 결과는 사용자의 소유입니다. 로컬에 저장하거나 대시보드와 통합하거나 CI 시스템에 연결할 수 있습니다.

## 멀티 에이전트 지원으로 더 빠르고 일관된 평가 수행

평가를 순차적으로 실행하면 느릴 수 있고 누적된 컨텍스트가 테스트 실행 사이에 유출될 수 있습니다. 이제 Skill-creator는멀티 에이전트 지원을 통해 독립적인 에이전트를 생성하여 평가를 동시에 실행합니다. 각 평가는 고유한 토큰과 타이밍 지표를 갖춘 깨끗한 컨텍스트에서 실행됩니다. 더 빠른 결과 확인, 교차 오염 없음

또한 A/B 비교를 위한Comparator 에이전트를 추가했습니다. 두 가지 skill 버전을 비교하거나 skill을 사용하지 않는 경우와 skill을 사용하는 경우를 비교합니다. 어떤 결과물이 어떤 것인지 모른 채 결과물을 판단하므로 변경이 실제로 도움이 되었는지 여부를 판단할 수 있습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a74e0afa8435f070120ed9_skillscreator-AB-testing-1920x1080-v1.png)

## 적절한 시점에 skill이 트리거되도록 하기

평가는 결과물의 품질을 측정하지만, 이는 skill이 필요할 때 트리거되는 경우에만 중요합니다. skill 수가 증가함에 따라 설명의 정밀도가 더 중요해집니다. 설명이 너무 광범위하면 잘못 트리거되고 설명이 너무 편협하면 skill이 절대 실행되지 않습니다. 이제 Skill-creator는 더 신뢰할 수 있는 Skill 트리거를 위해 설명을 조정하도록 지원합니다. 샘플 프롬프트와 비교해 현재 설명을 분석하고, 오작동과 미작동을 모두 줄일 수 있는 수정 사항을 제안합니다.

document-creation skill 전반적에서 실행하여 공개 skill 6개 중 5개 skill의 트리거가 개선된 것을 확인했습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69a74e1f72940942cb534904_skillscreator-skill-description-optimization-results.png)

## 미래 전망

모델이 개선되면 'skill'과 '사양' 사이의 경계가 모호해질 수 있습니다. 현재, SKILL.md 파일은 본질적인 구현 계획으로, Claude에게수행 방식을 알려주는 상세한 지침을 제공합니다. 시간이 지나면 skill이 수행해야 하는작업에 대한 자연어 설명으로도 충분할 수 있으며, 나머지는 모델이 처리해 줍니다.

오늘 발표하는 eval 프레임워크는 그러한 방향으로 나아가는 한 걸음입니다. Eval은 이미 그 '작업'을 설명합니다. 결국 그 설명이 skill 자체가 될 수 있습니다.

## 시작하기

모든 skill-creator 업데이트는 이제 Claude.ai와 Cowork에서 사용할 수 있습니다. Claude에게 skill-creator를 사용하여 시작하기에 대해 질문하세요.

Claude Code 사용자는[플러그인](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/skill-creator)을 설치하거나 Claude[리포지토리](https://github.com/anthropics/skills/tree/main/skills/skill-creator)에서 다운로드할 수 있습니다.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229e73ca2d0d73d78f7_682ac293884c9d4ee4ebe2355a2f6c4ecfdd9c1b-1000x1000.svg)

### Getting started with loops

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

### AI가 COBOL 현대화의 비용 장벽을 극복하도록 지원하는 방법

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

### 데스크톱용 Claude Code에 자동화된 미리보기, 검토, 병합 기능 도입

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/improving-skill-creator-test-measure-and-refine-agent-skills
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
