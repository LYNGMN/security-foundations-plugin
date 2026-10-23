# Security Foundations 플러그인

조직의 보안 자세를 기본기부터 진단하고, 증거로 뒷받침되는 통제 계획을 만드는 자문형 스킬입니다. 매번 네 가지를 산출합니다: 자산·사각지대 진단, 표준 근거가 붙은 통제 매트릭스, 실행 런북, 검증과 잔여 위험.

정렬 기준: NIST CSF 2.0, ISO/IEC 27001:2022, NIST SP 800-61r3, SP 800-63B Rev.4, OWASP Top 10 for Agentic Applications 2026, SLSA v1.2.

## 폴더 구성

```
security-foundations-plugin/
├── .claude-plugin/
│   ├── plugin.json             Claude 플러그인 매니페스트
│   └── marketplace.json        로컬 마켓플레이스 (폴더째 설치용)
├── skills/security-foundations/
│   ├── SKILL.md                영어판 (기본)
│   ├── SKILL.ko.md             한국어 미러 (둘을 함께 로드하지 않음)
│   ├── references/             실패 모드, 표준 지도, 사고 런북
│   └── evals/evals.json        트리거·루브릭 평가 케이스
├── commands/
│   ├── foundations-check.md    Claude 슬래시 명령
│   └── foundations-check.toml  Gemini CLI 명령
├── AGENTS.md                   Codex 등 AGENTS.md를 읽는 도구용
├── GEMINI.md                   Gemini CLI 컨텍스트
├── gemini-extension.json       Gemini CLI 확장 매니페스트
├── adapters/
│   ├── core-instructions.md    ChatGPT·Gemini용 압축 지침 (8,000자 이내)
│   ├── chatgpt-custom-gpt/README.md
│   └── gemini-gem/README.md
├── claude-ai-upload/security-foundations.skill   Claude 앱 업로드용
└── scripts/validate_and_package.py               검증 + zip 생성
```

## 환경별 사용법

설치 절차는 작성 시점 기준이며 각 도구의 버전에 따라 달라질 수 있습니다. 이 패키지를 만든 환경에서는 각 도구에 실제로 설치해 보지 못했고, 파일 형식과 길이만 검증했습니다.

| 환경 | 형태 | 사용하는 파일 |
|---|---|---|
| Claude Code / Cowork | 플러그인 | `.claude-plugin/`, `skills/`, `commands/` |
| Claude 앱 (웹·데스크톱·모바일) | 스킬 업로드 | `claude-ai-upload/security-foundations.skill` |
| ChatGPT | Custom GPT | `adapters/core-instructions.md` + 지식 파일 4개 |
| Gemini 웹 앱 | Gem | 위와 동일 |
| Gemini CLI | 확장 | `gemini-extension.json`, `GEMINI.md`, `commands/*.toml` |
| Codex 등 | AGENTS.md | `AGENTS.md` + `skills/` 폴더 |

### Claude Code
```
/plugin marketplace add ./security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```
설치 후 스킬은 보안 관련 질문에서 자동으로 불리고, `/security-foundations:foundations-check <점검 대상>`으로 직접 실행할 수도 있습니다.

### Claude 앱
`claude-ai-upload/security-foundations.skill`을 스킬 업로드 기능으로 올립니다.

### ChatGPT, Gemini Gem
각 폴더의 README(`adapters/chatgpt-custom-gpt/README.md`, `adapters/gemini-gem/README.md`)를 따라 지침을 붙여 넣고 지식 파일을 올립니다.

## 환경별 차이

Claude 스킬은 필요할 때 자동으로 불리고 참조 파일도 필요한 시점에만 읽습니다. ChatGPT와 Gemini의 Gem은 지침과 지식 파일에 의존하므로 같은 규칙이 덜 엄격하게 지켜질 수 있습니다. 그래서 압축 지침에는 4섹션 형식, 격리 → 보존 순서, 중단 규칙을 본문에 직접 넣었습니다. Custom GPT와 Gem에는 파일·셸 접근이 없어 자격 증명 열람 금지 같은 규칙은 사용자가 파일을 붙여 넣는 상황에서만 작동합니다.

## 원문 대비 바뀐 점

- 프런트매터: `version`, `language`를 `metadata:` 아래로 옮겼습니다(Claude의 스킬 검증이 허용하지 않는 최상위 키였습니다). `compatibility`를 추가했습니다.
- description: 사용자가 보안 용어를 직접 쓰지 않아도 발동하도록 트리거 문구(랜섬웨어, ISMS-P, SBOM, MCP 가드레일 등)를 넣었고, 한국어 키워드를 한국어판에 반영했습니다. 1,024자 이내입니다.
- 응답 언어 섹션을 추가했습니다(사용자 언어로 답하고 표준 식별자는 원문 유지).
- 한국어판의 오타를 고쳤습니다: ASI10 "로그 에이전트" → "이탈(rogue) 에이전트".
- 확인되지 않은 두 항목을 바로잡았습니다. 'SHIELD 2026' 프레임워크는 공개된 표준을 찾지 못해 "내부 체크리스트"로 바꿨고(안티패턴 문구 포함), MITRE ATLAS는 v5.4.0 기준 16 전술·84 기법·56 하위 기법으로 고쳤습니다(원문의 "14 agentic"은 2025년 10월 추가분 수치였습니다). `references/standards-map.md` 끝의 검증 노트를 참고하세요.

## 검증과 배포

```
python3 scripts/validate_and_package.py [출력 폴더]
```

JSON·프런트매터·버전 일치·참조 파일·지침 길이(8,000자)를 검사한 뒤 zip을 만듭니다. `evals/evals.json`의 케이스는 Claude Code의 skill-creator 평가 루프나 `claude plugin eval` 계열 도구에서 쓰도록 원문 그대로 두었습니다.

## GitHub에 올리고 설치하기

```
gh auth login
bash scripts/publish-to-github.sh security-foundations-plugin --private
```

스크립트는 검증을 통과해야 push합니다. 기본값은 비공개이며, `--public`은 `LICENSE` 파일이 있어야 진행됩니다. 올린 뒤 설치 명령은 다음과 같습니다(`OWNER`는 GitHub 사용자명).

| 도구 | 명령 |
|---|---|
| Claude Code | `/plugin marketplace add OWNER/security-foundations-plugin` 다음 `/plugin install security-foundations@security-foundations-marketplace` |
| Gemini CLI | `gemini extensions install https://github.com/OWNER/security-foundations-plugin` |
| Codex | 저장소를 clone해 `skills/security-foundations`를 `~/.agents/skills/`에 복사 |
| ChatGPT, Gemini Gem, Claude 앱 | GitHub 설치 없음. `adapters/` README 또는 `.skill` 업로드 |

## 평가 결과 (2026-10-23)

`skills/security-foundations/evals/` 아래 4개 케이스를 스킬 있음·없음으로 1회씩 실행하고 13개 검증 항목을 채점했습니다.

| 구성 | 통과 | 통과율 |
|---|---|---|
| 스킬 있음 | 12 / 13 | 92% |
| 스킬 없음 | 7 / 13 | 54% |

- 차이가 큰 곳: 공급망·에이전트 계획(4/4 대 1/4). 스킬 없이는 4섹션 구조, SLSA v1.2 Source Track과 L3, ASI01~ASI10 식별자가 빠졌습니다.
- 스킬이 틀린 곳: 피싱 대응에서 CSF 2.0 여섯 기능 매핑을 드러내지 않았습니다. 규칙 8에 매핑 명시 문장을 추가하고 이 케이스만 다시 실행해 3/3으로 확인했습니다(나머지 케이스는 재실행하지 않았습니다).
- 차이가 없는 곳: 자격 증명 열람 거부 케이스는 스킬 없이도 3/3이라 변별력이 없습니다. 더 강하게 유도하는 프롬프트를 추가해야 합니다.
- 한계: 케이스당 1회 실행이고 채점은 같은 세션에서 했습니다. 통과율은 방향을 보여 주는 값이지 통계적 결론이 아닙니다. 트리거 정확도(`evals.json`의 `trigger_tests`)와 description 최적화는 실행하지 않았습니다.

## 라이선스

라이선스는 아직 지정하지 않았습니다. 배포 전에 `plugin.json`의 `license`와 저작자 정보를 정해 주세요.
