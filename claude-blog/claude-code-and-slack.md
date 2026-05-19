# Claude Code와 Slack
*May 19, 2026*
---
![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/692f7912d5b05a5c7ed8ae86_Object-CodeChatCode.svg)

# Claude Code와 Slack

- 카테고리제품 발표

- 제품Claude Code

- 날짜2025-12-08

- 읽는 시간5분

- 공유링크 복사https://claude.com/blog/claude-code-and-slack

오늘 Slack에서 바로 Claude Code에 작업을 위임할 수 있는 기능이 도입되었습니다. 이제 리서치 프리뷰 형태로 제공되는 이 베타 버전으로, Claude는 Slack 대화에서의 맥락을 코딩 세션으로 손쉽게 옮길 수 있습니다.

## 논의에서 구현까지

버그 보고서, 기능 요청, 엔지니어링 논의 등 엔지니어링 작업과 관련된 중요한 맥락은 대부분 Slack 내에 존재합니다. 버그가 보고되거나 팀원이 코드 수정을 요청할 때, 이제 Slack에서 Claude를 태그하면 주변 맥락을 활용해 Claude Code 세션이 자동으로 시작됩니다. 다음 상황에 사용하세요.

- 버그 조사 및 수정: 버그 신고가 접수되면 즉시 조사하고 수정하도록 Claude에 요청하세요.

- 빠른 코드 검토 및 수정: Claude가 팀 피드백을 바탕으로 소규모 기능을 구현하거나 코드를 리팩터링하도록 요청합니다.

- 협업 디버깅: 팀 논의에서 나온 오류 재현이나 사용자 리포트와 같은 중요한 맥락을 바탕으로, Claude 디버깅 전략을 수립합니다.

## Claude Code에 자동으로 작업을 라우팅합니다

이 기능은 기존[Slack용 Claude 앱](https://www.claude.com/blog/claude-and-slack)을 확장하여, Claude가 Claude Code 웹 환경으로 작업을 다시 전달할 수 있도록 합니다. Slack에서 @Claude를 멘션하면, Claude는 메시지를 검토하여 코딩 작업인지 여부를 확인합니다. 코딩 작업이라면 새 Claude Code 세션이 자동으로 생성됩니다. 또한 요청을 코딩 작업으로 처리하도록 Claude에 수동으로 지시할 수 있습니다.

Claude는 Slack에서 최근 채널과 스레드 메시지의 맥락을 수집하고, Claude Code 세션에 반영합니다. 이 맥락을 활용하여, 웹에서 Claude Code에 인증된 리포지토리를 기반으로 작업을 실행할 리포지토리를 자동으로 선택합니다.

Claude Code 세션이 진행되면서, Claude는 Slack 스레드에 상태 업데이트를 다시 게시합니다. 작업이 완료되면, 변경 사항을 검토할 수 있는 전체 세션에 대한 링크와 풀 리퀘스트(PR)를 즉시 열 수 있는 링크를 확인할 수 있습니다.

## 시작하기

시작하려면[Slack App Marketplace](https://slack.com/marketplace/A08SF47R6P4)에서 Claude 앱을 Slack 워크스페이스에 설치하세요. 설치가 완료되면 Claude 계정으로 인증하고, 코딩 작업에 @Claude를 멘션합니다. Claude가 코딩 작업을 라우팅하려면[웹에서 Claude Code](https://www.claude.com/blog/claude-code-on-the-web)에 액세스해야 합니다.

자세한 내용은[문서를 확인하세요](https://code.claude.com/docs/en/slack).

‍

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

![](https://cdn.prod.website-files.com/6889473510b50328dbb70ae6/6889473610b50328dbb70b58_placeholder.svg)

자주 묻는 질문

## 관련 게시물

Claude로 구축하는 팀을 위한 더 많은 제품 뉴스와 모범 사례를 살펴보세요.

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22bed4b18b6703cd710_e750c875fbd7f08ffb6495efa180a8ed60de3611-1000x1000.svg)

### New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d22e13864f88ea55c2d8_b5c98d26c46edc43193e7f7e28a00633a538bb9c-1000x1000.svg)

### Code w/ Claude SF 2026 recap: Building on the AI exponential

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6a025cf25f0694905405e054_Object-Scale.svg)

### Claude for the legal industry

![](https://cdn.prod.website-files.com/68a44d4040f98a4adf2207b6/6903d2308749b4e883cc44b7_e029027e0b3beeb5b629bd4a26143597e7775b38-1000x1000.svg)

### Claude Security is now in public beta

## Claude와 함께 조직의 운영 방식을 혁신하세요

개발자 뉴스레터 구독

제품 업데이트, 사용 방법, 커뮤니티 스포트라이트 등 다양한 소식을 전해드립니다. 매달 이메일로 받아보세요.

월간 개발자 뉴스레터를 받고 싶으시다면 이메일 주소를 입력하세요. 언제든지 구독 취소할 수 있습니다

---
**Source:** https://claude.com/ko/blog/claude-code-and-slack
*This is a mirror of the Claude.com blog post for local access and AI-assisted development.*
