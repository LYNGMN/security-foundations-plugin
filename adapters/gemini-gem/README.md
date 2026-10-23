# Gemini Gem 설정

1. Gemini 웹 앱에서 새 Gem을 만듭니다 (Gem 관리자 → 새 Gem).
2. **이름**: Security Foundations Advisor
3. **지침**: `../core-instructions.md` 전체를 붙여 넣습니다.
4. **지식 파일**: 아래를 업로드합니다. 영어판만 올리면 충분합니다.
   - `skills/security-foundations/SKILL.md`
   - `skills/security-foundations/references/standards-map.md`
   - `skills/security-foundations/references/failure-modes.md`
   - `skills/security-foundations/references/incident-runbook.md`
5. 저장 후 아래 문장으로 동작을 확인합니다.
   - 외부 AI 에이전트와 MCP 서버를 도입하려 합니다. 가드레일과 승인 게이트를 설계해 주세요.

## Gemini CLI에서 쓰는 경우

이 폴더 루트에 있는 `gemini-extension.json`, `GEMINI.md`, `commands/foundations-check.toml`이 확장(extension) 형태입니다.

```
gemini extensions install ./security-foundations-plugin
```

개발 중에는 `gemini extensions link ./security-foundations-plugin`처럼 링크로 연결할 수 있습니다. 명령 이름과 옵션은 Gemini CLI 버전에 따라 다를 수 있으니 `gemini extensions --help`로 확인하세요. 설치 후 `/foundations-check <점검 대상>`으로 실행합니다.

## 알아둘 점

- Gem은 지침 기반이라 Claude 스킬처럼 규칙이 강제되지는 않습니다.
- 지식 파일은 질문과 관련된 부분만 불러오므로, 4섹션 출력 형식과 중단 규칙은 지침 본문에 그대로 들어 있습니다.
