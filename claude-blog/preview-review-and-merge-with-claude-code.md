# 데스크톱용 Claude Code에 자동화된 미리보기, 검토, 병합 기능 도입
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22a9e09b6cfb6289430_c9d8dd2af6d065e1ace8bd4bb29c716eb53ffffb-1000x1000.svg)

# 데스크톱용 Claude Code에 자동화된 미리보기, 검토, 병합 기능 도입

데스크톱용 Claude Code 업데이트로 개발 흐름을 긴밀하게 연결하여, 코드 작성부터 PR 병합까지 한 곳에서 진행할 수 있습니다.

- 카테고리Claude Code제품 발표

- 제품Claude Code

- 날짜2026-02-20

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/preview-review-and-merge-with-claude-code

오늘, Claude Code에 여러 개선 사항을 적용해, 실행 중인 앱 미리보기, 코드 자동 리뷰, PR 자동 수정 및 병합, 데스크톱/모바일/CLI 간의 원활한 전환 기능을 선보입니다. 이러한 업데이트를 통해 코드와 관련된 번거로운 작업에 드는 시간을 줄이고, 더 즐기고 싶은 일에 더 많은 시간을 쓸 수 있습니다.

## 코드를 작성하고 실행 결과를 확인하세요

이제 데스크톱용 Claude Code에서 개발 서버를 구동하고, 실행 중인 앱을 데스크톱 인터페이스에서 직접 미리 볼 수 있습니다. Claude는 웹앱 UI를 확인하고, 콘솔 로그를 읽으며, 오류를 감지하여 계속 개선해 나가므로, 브라우저에서 보이는 내용을 Claude에게 따로 설명할 필요가 없습니다. 또한 미리보기 화면에서 시각적 요소를 선택하고, 피드백을 Claude에 바로 전달해 지속적으로 개선할 수도 있습니다.

## 푸시 전에 코드를 검토하세요

변경 사항이 정리되면, 새롭게 추가된 "Review code" 버튼으로 Claude에게 검토를 요청할 수 있습니다. Claude는 로컬 diff를 검토하고 데스크톱 diff 화면에 직접 코멘트를 남겨 버그를 찾아내고, 개선점을 제안하며, 잠재적인 문제를 코드상에서 바로 찾아줍니다.

이제 코드가 외부로 나가기 전에 눈에 띄는 문제를 한 번 더 확인할 수 있고, Claude에게 코드에 달린 코멘트를 반영해 직접 수정하도록 요청할 수도 있습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6998ab6c581b7e1365118a98_Code%20Review.png)

## 앱을 벗어나지 않고 PR을 모니터링하세요

GitHub에서 호스팅된 코드의 경우, 데스크톱 앱에서 직접 PR 상태를 모니터링할 수도 있습니다. PR을 열면, Claude Code가 내부적으로 GitHub CLI를 사용하여 CI 검사 통과와 실패 여부를 포함한 상태를 추적합니다.

또한 auto-fix를 활성화하면 Claude가 탐지한 CI 실패를 자동으로 해결하려고 시도합니다. auto-merge를 활성화하면, Claude는 모든 검사가 통과된 후 PR 병합까지 진행하려고 시도합니다.

Claude Code 세션에서 하나의 작업을 수행해 PR을 연 다음, 곧바로 새로운 작업을 진행할 수 있습니다. 그 사이 Claude Code는 백그라운드에서 원래 작업의 PR을 모니터링하고, CI 실패를 수정하려고 시도합니다. 그래서 다시 해당 작업으로 돌아올 때쯤이면 PR이 병합 준비가 되어 있거나, 이미 자동으로 병합되어 있을 수 있습니다.

![__wf_reserved_inherit](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6998ab7b361d36cb996e0cc8_CI%20Monitoring.png)

## 중단한 지점부터 이어서 진행하세요

이제 세션은 사용자를 따라 이동합니다. CLI의 Claude Code에서 세션을 시작한 뒤 /desktop을 실행하면, 전체 세션 컨텍스트를 데스크톱 앱으로 가져올 수 있습니다.

또한 "Continue with Claude Code on the web(웹에서 Claude Code 계속 진행)" 버튼을 사용하면 로컬 데스크톱 앱 세션을 클라우드로 전환할 수 있습니다. 데스크톱 앱에서 시작한 작업을 웹이나 휴대폰의 Claude 모바일 앱에서 그대로 이어 진행할 수 있습니다.

## 시작하기

이제 이러한 업데이트는 모든 사용자가 활용할 수 있습니다. 시작하려면[데스크톱에서 Claude Code](https://claude.com/download)를 업데이트하거나 다운로드하세요. 자세한 내용은[문서](https://code.claude.com/docs/en/desktop)를 확인해 보세요.

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f76874e94e489958af8ba_Object-CodeMagnifier.svg)

### AI가 COBOL 현대화의 비용 장벽을 극복하도록 지원하는 방법

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22930b7622d6096c33d_4d663bd87c391c144b9bca513b3849ccfa00a3b9-1000x1000.svg)

### 이제 Opus 4.6과 Sonnet 4.6에서 1M 컨텍스트를 정식 지원합니다

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2287f90c57df4c9dd97_c1ef4c0b6882dfe985555b52999d370ea88a3c50-1000x1000.svg)

### skill-creator 개선: Agent Skills 테스트, 측정 및 개선

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d229a7aa26ac1b6e96c2_a62b6eb169818f14c35b7a192af269e283f8fa93-1000x1000.svg)

### 동적 필터링을 통해 웹 검색 정확도와 효율성 향상

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/preview-review-and-merge-with-claude-code
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
