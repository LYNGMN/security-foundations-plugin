# ChatGPT Custom GPT 설정

1. ChatGPT에서 새 GPT를 만듭니다 (GPT 만들기 → 구성).
2. **이름**: Security Foundations Advisor
3. **설명**: 조직의 보안 자세를 기본기부터 진단하고 증거 기반 통제 계획을 만들어 줍니다.
4. **지침(Instructions)**: `../core-instructions.md` 전체를 붙여 넣습니다. 8,000자 이내로 맞춰져 있습니다(`scripts/validate_and_package.py`가 길이를 검사합니다).
5. **지식(Knowledge) 파일**: 아래 4개를 업로드합니다. 영어판만 올리면 충분하며 `SKILL.ko.md`는 중복이라 올리지 않습니다.
   - `skills/security-foundations/SKILL.md`
   - `skills/security-foundations/references/standards-map.md`
   - `skills/security-foundations/references/failure-modes.md`
   - `skills/security-foundations/references/incident-runbook.md`
6. **기능**: 코드 인터프리터와 이미지 생성은 필요 없습니다. 웹 검색은 표준 버전 확인용으로 켜 두면 좋습니다.
7. **대화 시작 예시(Conversation starters)**:
   - 외부 AI 에이전트와 MCP 서버를 도입하려 합니다. 가드레일과 승인 게이트를 설계해 주세요.
   - 직원이 피싱 첨부파일을 열었고 PC가 이상하게 동작합니다. 초동 대응 순서를 알려 주세요.
   - 레거시 시스템과 서드파티 패치 프로세스를 감사하고 개선 우선순위를 정해 주세요.
   - CISA KEV에 오른 긴급 패치가 나왔는데 공급망 위험 때문에 7일 기다려야 할까요?

## 알아둘 점

- GPT는 지침과 지식 파일에 의존하므로 Claude 스킬처럼 규칙이 강제되지는 않습니다. 핵심 규칙(4섹션, 격리 → 보존 순서, 중단 규칙)을 지침 본문에 직접 넣은 이유입니다.
- Custom GPT에는 파일 시스템이나 셸 접근이 없으므로 `.env` 열람 금지 같은 중단 규칙은 사용자가 파일을 붙여 넣을 때만 의미가 있습니다.
- 지식 파일은 검색으로 일부만 불러올 수 있으니, 중요한 판단은 지침 본문의 규칙을 기준으로 합니다.
