# 동적 필터링을 통해 웹 검색 정확도와 효율성 향상
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

# 동적 필터링을 통해 웹 검색 정확도와 효율성 향상

동적 필터링 덕분에 Claude는 복잡한 웹 검색 작업에서 더 정확하고 효율적으로 작동합니다. 다음은 Claude의 작동 방식과 API에서 Claude를 활성화하는 방법입니다.

- 카테고리제품 발표

- 제품Claude Platform

- 날짜2026-02-17

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/improved-web-search-with-dynamic-filtering

Claude[Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)및[Sonnet 4.6](https://www.anthropic.com/news/claude-sonnet-4-6)과 함께[웹 검색](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)및[웹 가져오기](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)도구의 새 버전을 출시합니다. 이제 Claude는 [웹 검색](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) 중에 기본적으로 코드를 작성하고 실행하여 결과가 컨텍스트 창에 도달하기 전에 필터링할 수 있으므로 정확도와 토큰 효율성이 향상됩니다.

## 동적 필터링을 사용한 웹 검색

웹 검색은 토큰을 많이 사용하는 작업입니다. 기본 웹 검색 도구를 사용하는 에[이전](https://www.anthropic.com/engineering/advanced-tool-use)트는 쿼리를 작성하고 검색 결과를 컨텍스트로 가져오고 여러 웹사이트에서 전체 HTML 파일을 가져온 다음 응답하기 전에 이 모든 것을 추론해야 합니다. 그러나 검색에서 가져오는 컨텍스트는 관련성이 없는 경우가 빈번해 응답의 품질이 저하되는 경우가 많습니다.웹 검색에서 Claude의 성능을 향상시키기 위해 이제 웹 검색과 웹 가져오기 도구는 쿼리 결과를 후처리하기 위한 코드를 자동으로 작성하고 실행합니다. Claude는 전체 HTML 파일을 추론하는 대신, 컨텍스트에 로드하기 전에 검색 결과를 동적으로 필터링하여 관련 항목만 유지하고 나머지는 버릴 수 있습니다.이 기법이 다른 에[이전](https://www.anthropic.com/engineering/advanced-tool-use)틱 워크플로우에서 효과적인 것으로[이전](https://www.anthropic.com/engineering/advanced-tool-use)에 확인했으며, API에서 네이티브 지원을 위해[코드 실행](http://docs.anthropic.com/en/docs/agents-and-tools/tool-use/code-execution-tool)과[프로그래밍 방식의 도구 호출](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)과 같은 도구를 추가했습니다. 이제 웹 검색과 웹 가져오기에 동일한 기법을 적용하고 있습니다.

## Claude의 웹 검색 기능 평가

다른 도구는 활성화하지 않은 상태에서 동적 필터링을 적용한 경우와 적용하지 않은 경우로 나누어 Sonnet 4.6과 Opus 4.6에서 웹 검색을 평가했습니다.[BrowseComp](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf)와[DeepsearchQA](https://storage.googleapis.com/deepmind-media/DeepSearchQA/DeepSearchQA_benchmark_paper.pdf)라는 두 가지 벤치마크에서 동적 필터링은 성능은 평균 11% 향상되었고 동시에 입력 토큰 사용량은 24% 줄었습니다.[BrowseComp](https://cdn.openai.com/pdf/5e10f4ab-d6f7-442e-9508-59515c65e35d/browsecomp.pdf): 웹을 검색해 하나의 답변 찾기

BrowseComp는 에이전트가 여러 웹사이트를 탐색해 고의적으로 찾기 어렵게 만든 특정 정보를 온라인에서 찾을 수 있는지 테스트합니다. 동적 필터링을 통해 Claude의 정확도가 크게 향상되어 Sonnet 4.6은 33.3%에서 46.6%로, Opus 4.6은 45.3%에서 61.6%로 향상되었습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fbbb7eec8e454d86c9d_Dynamic-filtering-on-browsecomp.png)

DeepsearchQA: 웹을 검색해 다양한 답변 찾기

DeepsearchQA는 에이전트에게 많은 정답이 포함된 리서치 쿼리를 제공하며 모든 정답은 웹 검색을 통해 찾을 수 있어야 합니다. 에이전트가 답변을 놓치지 않으면서 다단계 검색을 체계적으로 계획하고 실행할 수 있는지 테스트합니다. 이는 정밀도와 재현율의 균형을 나타내는 'F1 점수'로 측정되며, 반환된 답변의 정확도와 검색의 완전성을 모두 포착합니다.

동적 필터링 덕분에 Claude의 F1 점수는 Sonnet 4.6의 경우 52.6%에서 59.4%로, Opus 4.6의 경우 69.8%에서 77.3%로 개선되었습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/69937fcede000ba1d5aab33d_Dynamic-filtering-on-DeepsearchQA.png)

토큰 비용은 모델이 컨텍스트를 필터링하기 위해 작성해야 하는 코드의 양에 따라 달라질 수 있습니다. 가격 가중 토큰은 두 벤치마크에서 Sonnet 4.6의 경우 감소했지만, Opus 4.6의 경우 증가했습니다. 비용을 더 잘 이해하기 위해, 에이전트가 프로덕션 환경에서 접할 가능성이 있는 대표적인 웹 검색 쿼리 세트와 비교해 이 도구를 평가하는 것이 좋습니다.

## 고객 사례 소개: Quora

[Poe](https://poe.com)by[Quora](https://quora.com)는 최대 규모의 멀티 모델 AI 플랫폼 중 하나로, 수백만 명의 사용자가 단일 인터페이스를 통해 200개가 넘는 모델에 액세스할 수 있도록 지원합니다. [Quora](https://quora.com)의 내부팀은 동적 필터링이 적용된 Opus 4.6이 "다른 최첨단 모델과 비교해 테스트했을 때 내부 평가에서 가장 높은 정확도를 달성했다"는 사실을 발견했다고 제품 및 리서치 리드인 Gareth Jones가 말했습니다. "모델은 실제 연구원처럼 작동하며 컨텍스트에서 원시 HTML을 추론하기보다는 결과를 분석하고 필터링하고 상호 참조하도록 Python을 작성합니다."

## 웹 검색 및 가져오기 도구에서 동적 필터링

Claude API에서 Sonnet 4.6과Opus 4.6과 함께 새로운 웹 검색 및 웹 가져오기 도구를 사용할 때는 동적 필터링이 기본적으로 켜집니다. 기술 문서를 선별하거나 인용 검증과 같은 복잡한 웹 검색 쿼리의 경우에는 위 그림과 유사한 성능 향상을 기대할 수 있습니다.

API에서 동적 필터링을 사용하는 방법은 다음과 같습니다.

```

```

## 이제 코드 실행, 메모리 등 더 많은 도구가 제공됨

또한 여러 도구를 정식 출시하여 토큰 사용량 많은 작업에서 에이전트가 더 뛰어난 성능을 발휘할 수 있도록 지원합니다.

- 코드 실행:에이전트가 컨텍스트 필터링, 데이터 분석 또는 계산을 위해 대화 중에 코드를 실행할 수 있는 샌드박스를 제공합니다.

- 메모리: 영구 파일 디렉터리를 통해 여러 대화 간 정보를 저장하고 검색하므로 에이전트가 컨텍스트 창에 모든 정보를 저장하지 않아도 컨텍스트를 유지할 수 있습니다.

- 프로그래밍 방식 도구 호출:복잡한 멀티 도구 워크플로우를 코드에서 실행하고 중간 결과는 컨텍스트 창 외부로 유지합니다.

- 도구 검색:모든 정의를 컨텍스트 창에 로드하지 않고 대규모 라이브러리에서 도구를 동적으로 검색할 수 있습니다.‍

- 도구 사용 예시:도구 정의에 직접 도구 호출 샘플을 포함하여 사용 패턴을 보여줘 매개변수 오류를 줄일 수 있습니다.

### 시작하기

이제 Claude Platform에서 향상된 웹 검색 및 웹 가져오기와 코드 실행, 메모리, 프로그래밍 방식 도구 호출, 도구 검색, 도구 사용 예시를 사용할 수 있습니다.[API 문서](https://platform.claude.com/docs/en/build-with-claude/overview)를 읽고 시작해 보세요.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229b7f170bab528846d_0df729ce74e4c9dd62c3342c9549ce6c7cef1202-1000x1000.svg)

### Bringing MCP 2026-07-28 to Claude

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

### skill-creator 개선: Agent Skills 테스트, 측정 및 개선

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

### 데스크톱용 Claude Code에 자동화된 미리보기, 검토, 병합 기능 도입

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/improved-web-search-with-dynamic-filtering
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
