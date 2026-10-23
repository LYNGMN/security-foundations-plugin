# Security Foundations

[English](README.md) · **한국어** · [简体中文](README.zh-CN.md) · [日本語](README.ja.md)

[![Release](https://img.shields.io/github/v/release/LYNGMN/security-foundations-plugin)](https://github.com/LYNGMN/security-foundations-plugin/releases/latest)
[![Validate](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

AI 어시스턴트에 붙이는 보안 자문가입니다. 보안 고민을 평소 말로 물어보면 경험 많은 보안 책임자처럼 답합니다. 먼저 실제로 무엇을 가지고 있는지부터 파악하고, 바로 실행하고 점검할 수 있는 계획을 내놓습니다.

**Claude**(앱과 Claude Code), **ChatGPT**, **Gemini**(웹과 CLI), **Codex**에서 쓸 수 있습니다. 질문한 언어로 답합니다.

## 무엇을 받게 되나요

답은 늘 같은 네 부분으로 나옵니다. 그래서 동료나 감사 담당자에게 그대로 넘길 수 있습니다.

| 부분 | 알려 주는 것 |
|---|---|
| 1. 자산과 사각지대 진단 | 무엇을 가지고 있는지, 주인이 없는 것은 무엇인지, 보호된다고 증명하지 못하는 것은 무엇인지 |
| 2. 통제 계획 | 계층별로 무엇을 갖출지, 항목마다 근거가 되는 표준과 운영에 드는 부담 |
| 3. 단계별 실행 순서 | 오늘 바로 따라 할 수 있는 번호 매긴 조치 |
| 4. 검증과 남는 위험 | 각 통제가 실제로 작동하는지 시험하는 방법과 아직 드러나 있는 위험 |

이런 질문으로 시작해 보세요.

- *"직원이 피싱 메일 첨부파일을 열었는데 PC가 이상하게 동작해요. 무엇부터 해야 하나요?"*
- *"AI 에이전트와 MCP 서버를 사내 시스템에 연결하려고 해요. 안전장치와 승인 절차를 설계해 주세요."*
- *"오래된 시스템과 외부 업체 패치 관리를 점검하고, 무엇부터 고칠지 알려 주세요."*
- *"실제로 공격에 쓰이는 취약점의 긴급 패치가 나왔어요. 공급망 위험 때문에 일주일 기다려야 할까요?"*
- *"ISO 27001 인증을 준비하고 있어요. 가장 크게 부족한 곳이 어디인가요?"*

IT·보안 담당자, 개발자, 보안 전담자가 없는 작은 팀의 대표와 관리자, 감사를 앞둔 분께 맞습니다.

## 설치

지금 AI를 쓰고 있는 곳을 고르세요. 위의 세 가지는 코딩을 몰라도 됩니다.

| 쓰는 곳 | 걸리는 시간 | 바로 가기 |
|---|---|---|
| Claude 앱 (웹·데스크톱·모바일) | 2분 | [Claude 앱](#claude-앱) |
| ChatGPT | 2분 | [ChatGPT](#chatgpt) |
| Gemini (웹) | 5분 | [Gemini](#gemini) |
| Claude Code | 1분 | [Claude Code](#claude-code) |
| Gemini CLI | 1분 | [Gemini CLI](#gemini-cli) |
| Codex | 1분 | [Codex](#codex) |

### Claude 앱

Claude 유료 요금제에서 코드 실행 기능이 켜져 있어야 합니다.

1. [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip)을 내려받습니다. 압축은 풀지 않습니다.
2. Claude에서 **설정(Settings) → 기능(Capabilities)** 으로 갑니다.
3. **스킬(Skills)** 에서 **스킬 업로드(Upload skill)** 를 누르고 내려받은 파일을 고릅니다.
4. 스킬이 켜져 있는지 확인합니다. 이제 아무 대화에서나 보안 질문을 하면 Claude가 알아서 이 스킬을 씁니다.

### ChatGPT

ChatGPT는 이제 플러그인을 씁니다(맞춤 GPT는 2026년 12월 11일 종료). ChatGPT 유료 요금제가 필요하며 Plus에서 확인했습니다.

1. [**security-foundations-chatgpt-plugin.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-chatgpt-plugin.zip)을 내려받습니다. 압축은 풀지 않습니다.
2. [chatgpt.com/plugins](https://chatgpt.com/plugins)에서 **추가(Add)** → **플러그인 압축 파일 업로드**를 고릅니다.
3. 파일을 끌어다 놓고 **플러그인 추가**를 누른 뒤, 열린 페이지에서 **플러그인 설치**를 누릅니다.
4. 대화창에 `@Security Foundations Advisor`와 질문을 함께 입력하거나, 플러그인 페이지의 예시 질문을 누릅니다.

나중에 업데이트하려면 플러그인 페이지에서 **⋯ → 새 버전 업로드**로 새 파일을 올립니다.

### Gemini

Gemini는 이제 Gem 대신 스킬을 씁니다. Gemini 웹과 Mac용 Gemini 앱에서 됩니다.

1. [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip)을 내려받아 압축을 풉니다. `security-foundations` 폴더가 생깁니다.
2. [gemini.google.com](https://gemini.google.com)에서 **설정(Settings) → 스킬(Skills)** 로 갑니다.
3. 스킬 가져오기를 고르고 폴더 안의 `SKILL.md` 파일을 선택합니다.
4. 권장: 새 스킬에 마우스를 올려 **스킬 작업(Skill actions) → 스킬 교체(Replace skill)** 를 누르고 `security-foundations` 폴더 전체를 고릅니다. 참고 파일까지 함께 들어갑니다.
5. 스킬이 켜져 있는지 확인합니다(교체하면 꺼질 수 있습니다). 대화창에서 질문 앞에 `@security-foundations`를 붙이면 Gemini가 이 스킬을 씁니다.

아직 스킬 메뉴가 없는 계정이라면 [security-foundations-instructions-kit.zip](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-instructions-kit.zip)로 [gemini.google.com/gems/create](https://gemini.google.com/gems/create)에서 Gem을 만드세요. `instructions.md`를 붙여 넣고 `knowledge` 파일 4개를 추가하면 됩니다.

### Claude Code

Claude Code에 아래 두 줄을 입력합니다.

```text
/plugin marketplace add LYNGMN/security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```

새 세션을 열면 `/` 메뉴에 두 항목이 보입니다.

| 항목 | 이럴 때 씁니다 |
|---|---|
| `/security-foundations:foundations-check` | **처음에는 이것부터.** 점검할 대상을 함께 쓰거나, 그냥 실행하면 범위를 묻는 질문부터 합니다. |
| `/security-foundations:security-foundations` | 거의 쓸 일이 없습니다. 평소 말로 보안 질문을 하면 알아서 쓰입니다. 자동으로 잡히지 않을 때만 직접 부르세요. |

Claude 앱에도 스킬을 올렸다면 데스크톱 앱에 `/anthropic-skills:security-foundations`가 하나 더 보일 수 있습니다. Claude 계정에 올린 같은 스킬이라 Claude Code에서는 무시해도 됩니다.

예시:

```text
/security-foundations:foundations-check 고객 데이터베이스와 백업 체계
```

### Gemini CLI

```bash
gemini extensions install https://github.com/LYNGMN/security-foundations-plugin
```

Gemini CLI를 다시 시작한 뒤 `/foundations-check <점검할 대상>`을 실행하거나 그냥 보안 질문을 하면 됩니다.

### Codex

```bash
git clone --depth 1 https://github.com/LYNGMN/security-foundations-plugin.git
mkdir -p ~/.agents/skills
cp -R security-foundations-plugin/skills/security-foundations ~/.agents/skills/
```

Codex를 다시 시작합니다. 나중에 업데이트하려면 내려받은 폴더에서 `git pull`을 실행하고 폴더를 다시 복사합니다.

## 어떻게 판단하나요

자문가는 열 가지 원칙을 따릅니다. 짧게 줄이면 이렇습니다.

1. **가진 것부터 파악합니다.** 장부에 등록된 것, 네트워크에서 실제로 발견되는 것, 보호된다는 증거가 있는 것을 비교하고, 무엇을 사기 전에 그 차이부터 메웁니다.
2. **새 도구보다 기본기가 먼저입니다.** 패치, 최소 권한, 다중 인증(MFA), 로그 보관, 복구까지 시험한 백업, 최신 자산 목록을 증거와 함께 갖춥니다.
3. **이유를 남깁니다.** 통제마다 왜 있는지 기록하고, 오래된 시스템에는 담당자를 정하고 폐기·유지·교체 중 하나로 결정합니다.
4. **공급망을 검증합니다.** 소프트웨어 구성 명세(SBOM)와 서명된 빌드 출처 증명을 요구합니다. 업체의 약속은 증거가 아닙니다.
5. **AI 에이전트의 권한을 제한합니다.** 에이전트마다 자율성 단계를 정해 그에 맞는 통제를 두고, 에이전트가 고칠 수 없는 비상 정지 장치를 마련하고, 모든 행동을 실제 사람과 연결합니다.
6. **제로 트러스트는 단계적으로 갑니다.** 사람이 손으로 하는 설정 대신 접근 판단을 자동화합니다.
7. **인식이 아니라 행동을 바꿉니다.** 실수한 그 순간에 알려 주고, 교육 이수율이 아니라 신고율을 재며, 피싱 훈련에 걸린 사람을 벌하지 않습니다.
8. **사고가 나면 먼저 격리합니다.** 접근을 끊고, 증거를 보존하고, 그다음에 조사합니다. 증거를 남기기 전에 포맷하거나 재부팅하지 않습니다.
9. **신뢰는 드러내서 얻습니다.** 빠르고 사실대로 알리고, 확인된 사실과 추정을 구분하며, 사고를 숨기지 않습니다.
10. **지켜야 할 의무에 맞춥니다.** 증거 한 벌로 NIST CSF, ISO 27001과 ISMS-P·DORA·NIS2 같은 지역 규제에 함께 대응합니다.

전체 규칙은 [skills/security-foundations/SKILL.md](skills/security-foundations/SKILL.md)(영어)와 [SKILL.ko.md](skills/security-foundations/SKILL.ko.md)(한국어)에 있습니다.

## 하지 않는 일

- 비밀번호, `.env` 파일, 개인 키 같은 자격 증명 읽기
- 검증되지 않은 소프트웨어 설치, 되돌릴 수 없는 명령 실행
- 악성코드나 익스플로잇 작성, 인증 우회 돕기
- 법률 의견 제시, 규정 준수 인증
- 증거 없이 안전하다고 말하기, 표준 번호를 지어내기

읽은 문서나 웹 페이지 안에 AI에게 내리는 지시가 들어 있으면, 따르지 않고 사용자에게 알립니다.

## 따르는 표준

| 분야 | 표준 |
|---|---|
| 보안 프로그램 | NIST Cybersecurity Framework (CSF) 2.0 |
| 관리 체계 | ISO/IEC 27001:2022 |
| 사고 대응 | NIST SP 800-61 Rev. 3 |
| 비밀번호와 인증 | NIST SP 800-63B Rev. 4 |
| 제로 트러스트 | CISA Zero Trust Maturity Model 2.0 |
| 소프트웨어 공급망 | SLSA v1.2, SBOM (SPDX, CycloneDX), CSAF/VEX |
| AI 에이전트 | OWASP Top 10 for Agentic Applications 2026, OWASP Top 10 for LLM 2025, MITRE ATLAS |
| AI 위험 관리 | NIST AI RMF, NIST AI 600-1 |

버전과 수치는 2026년 10월에 마지막으로 확인했습니다. 자세한 내용은 [standards-map.md](skills/security-foundations/references/standards-map.md)에 있습니다. 감사 보고서에 표준을 인용하기 전에는 원문에서 다시 확인하세요.

## 알아 두세요

- **조언만 하고 직접 손대지 않습니다.** 계획을 세우고 판단을 점검해 줄 뿐, 시스템을 스캔하거나 바꾸거나 고치지 않습니다.
- **전문가를 대신하지 않습니다.** 실제 사고가 났다면 보안팀이나 사고 대응 전문 업체에도 함께 연락하세요.
- **Gem이나 붙여 넣은 지침은 스킬보다 덜 엄격하게 따릅니다.** 붙여 넣은 지침에만 의존하기 때문에 가끔 한 부분을 빠뜨릴 수 있습니다. 그래서 네 부분 형식과 안전 규칙은 지침 본문에 직접 넣었습니다.
- **데이터는 쓰시는 AI 서비스에만 머뭅니다.** 이 프로젝트는 지침만 더할 뿐, 어디에도 데이터를 보내지 않습니다.

## 평가 결과

2026년 10월에 `claude plugin eval`로 측정했습니다. 케이스 9개를 스킬이 있을 때와 없을 때 각각 3번씩 돌렸습니다(Claude Code 2.1.303, 채점은 Claude Haiku).

| | 스킬 있음 | 스킬 없음 |
|---|---|---|
| 평균 점수 | **98%** | 51% |
| 써야 할 때 스킬이 쓰인 횟수 | 24번 중 24번 | — |
| 보안과 무관한 질문에 끼어들지 않은 횟수 | 3번 중 3번 | — |

차이가 가장 큰 곳은 공급망·에이전트 보안 계획(100% 대 7%), XDR 구매 승인 요청(100% 대 0%), 사람 없이 배포하는 에이전트(100% 대 20%), 피싱 초동 대응(93% 대 27%)입니다.

한 번씩 놓친 곳이 두 군데 남아 있습니다. 피싱 답변 하나에서 채점 모델이 CSF 2.0 매핑을 인정하지 않았고, 한국어 답변 하나는 담당자 지정이 부족하다고 판정됐습니다. 모델이 채점하므로 점수는 실행마다 조금씩 다릅니다. 케이스는 [evals/](evals/)에 있고, 아래 명령으로 직접 돌려 볼 수 있습니다.

## 기여하는 분께

```text
.claude-plugin/          Claude Code 플러그인과 마켓플레이스 매니페스트
skills/security-foundations/
  SKILL.md               스킬 본문 (영어, 기준본)
  SKILL.ko.md            검토용 한국어판
  references/            표준 지도, 실패 유형, 사고 대응 런북
evals/                   채점 기준이 있는 평가 케이스 (claude plugin eval)
commands/                Claude Code(.md)와 Gemini CLI(.toml)용 /foundations-check
adapters/                ChatGPT 플러그인 매니페스트, Gem·기타 채팅 도구용 지침(8,000자 이내)
AGENTS.md, GEMINI.md     Codex와 Gemini CLI용 컨텍스트 파일
gemini-extension.json    Gemini CLI 확장 매니페스트
scripts/                 검증과 패키징
```

배포 파일을 로컬에서 검증하고 만들려면(Python 3, 추가 설치 없음):

```bash
python3 scripts/validate_and_package.py
```

Claude Code에서 평가 케이스를 돌리려면:

```bash
claude plugin eval .
```

풀 리퀘스트를 환영합니다. `SKILL.md`, `SKILL.ko.md`, `adapters/core-instructions.md`의 내용을 서로 맞추고, PR을 열기 전에 검증 스크립트를 돌려 주세요. `.claude-plugin/plugin.json`의 버전과 같은 `v*` 태그를 올리면 릴리스가 자동으로 만들어지고, 릴리스 노트는 GitHub가 작성합니다.

보안 문제는 [SECURITY.md](SECURITY.md)의 방법으로 알려 주세요.

## 라이선스

[MIT](LICENSE) © 2026 Youngmin
