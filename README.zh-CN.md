# Security Foundations

[English](README.md) · [한국어](README.ko.md) · **简体中文** · [日本語](README.ja.md)

[![Release](https://img.shields.io/github/v/release/LYNGMN/security-foundations-plugin)](https://github.com/LYNGMN/security-foundations-plugin/releases/latest)
[![Validate](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

给你的 AI 助手配一位安全顾问。你用大白话提出安全问题，它会像经验丰富的安全负责人那样回答：先弄清你到底有什么，再给出一份能执行、能检查的计划。

支持 **Claude**（应用和 Claude Code）、**ChatGPT**、**Gemini**（网页版和命令行版）以及 **Codex**。你用什么语言提问，它就用什么语言回答。

## 你会得到什么

每个回答都分成相同的四个部分。你可以直接把它交给同事或审计人员。

| 部分 | 它告诉你什么 |
|---|---|
| 1. 资产与盲区诊断 | 你有哪些资产，哪些没人负责，哪些你无法证明已受保护 |
| 2. 控制措施计划 | 该落实什么，按层次列出，每一项都标明所依据的标准和对日常运营的影响 |
| 3. 分步操作手册 | 带编号的步骤，今天就能照着做 |
| 4. 验证与剩余风险 | 如何测试每项措施是否有效，以及还有哪些风险没有消除 |

可以试试这些问题：

- *"有员工打开了钓鱼邮件的附件，电脑现在行为异常。我们该先做什么？"*
- *"我们想把 AI 智能体和 MCP 服务器接入公司系统。请设计防护措施和审批流程。"*
- *"请审查我们的老旧系统和第三方补丁管理，告诉我们应该先修哪里。"*
- *"一个正在被利用的严重漏洞刚发布了补丁。因为有供应链风险，我们该等一周再打吗？"*
- *"我们正在准备 ISO 27001。最大的差距在哪里？"*

适合这些人使用：IT 和安全团队、开发者、创业者、没有安全专员的小团队负责人，以及正在准备审计的人。

## 安装

选一个你平时已经在用的 AI 工具。前三种不需要写代码。

| 你在用 | 用时 | 跳转 |
|---|---|---|
| Claude 应用（网页、桌面、手机） | 2 分钟 | [Claude 应用](#claude-app) |
| ChatGPT | 5 分钟 | [ChatGPT](#chatgpt) |
| Gemini（网页版） | 5 分钟 | [Gemini](#gemini) |
| Claude Code | 1 分钟 | [Claude Code](#claude-code) |
| Gemini CLI | 1 分钟 | [Gemini CLI](#gemini-cli) |
| Codex | 1 分钟 | [Codex](#codex) |

### Claude app

需要付费的 Claude 套餐，并且已开启代码执行功能。

1. 下载 [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip)。不要解压。
2. 在 Claude 中打开 **Settings → Capabilities**（设置 → 功能）。
3. 在 **Skills**（技能）中选择 **Upload skill**（上传技能），然后选中刚下载的文件。
4. 确认这个技能已打开。然后在任意对话中提出安全问题。问题合适时，Claude 会自己调用这个技能。

### ChatGPT

创建 GPT 需要付费的 ChatGPT 套餐。

1. 下载 [**security-foundations-chatgpt-kit.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-chatgpt-kit.zip) 并解压。
2. 打开 [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor)，进入 **Configure**（配置）标签页。
3. **Name**（名称）：`Security Foundations Advisor`
4. **Description**（描述）：`从基础出发诊断你的安全状况，并制定有证据支撑的控制措施计划。`
5. **Instructions**（指令）：打开工具包里的 `instructions.md`，复制全部内容，粘贴进去。
6. **Conversation starters**（对话开场白）：从[你会得到什么](#你会得到什么)中复制两三个问题。
7. **Knowledge**（知识库）：上传工具包 `knowledge` 文件夹里的四个文件。
8. **Capabilities**（功能）：保持 Web Search（网页搜索）开启。其他的用不到。
9. 选择 **Create**（创建）。除非你想分享给别人，否则选择 **Only me**（仅自己）。

### Gemini

Gemini 现在用技能（skills）取代了 Gem。适用于 Gemini 网页版和 Mac 版 Gemini 应用。

1. 下载 [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip) 并解压，会得到一个名为 `security-foundations` 的文件夹。
2. 打开 [gemini.google.com](https://gemini.google.com)，进入 **Settings → Skills**（设置 → 技能）。
3. 选择导入技能，然后选中文件夹里的 `SKILL.md` 文件。
4. 建议：把鼠标移到新技能上，选择 **Skill actions → Replace skill**（技能操作 → 替换技能），再选中整个 `security-foundations` 文件夹，这样参考文件也会一起加入。
5. 在对话中输入 `/security-foundations`，或者直接提出安全问题。问题合适时，Gemini 也会自动使用这个技能。

如果你的账号还没有技能功能，可以用 [ChatGPT 工具包](#chatgpt) 在 [gemini.google.com/gems/create](https://gemini.google.com/gems/create) 创建 Gem：粘贴 `instructions.md`，再添加 `knowledge` 里的四个文件。

### Claude Code

在 Claude Code 中输入下面两行：

```text
/plugin marketplace add LYNGMN/security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```

开启一个新会话。在 `/` 菜单里会看到两项：

| 条目 | 什么时候用 |
|---|---|
| `/security-foundations:foundations-check` | **从这里开始。** 在后面写上要审查的对象；如果什么都不写，它会先问几个确定范围的问题。 |
| `/security-foundations:security-foundations` | 一般用不到。用平常的话提出安全问题时，技能会自动运行。只有没被自动触发时才直接调用。 |

如果你也把技能上传到了 Claude 应用，桌面应用里可能还会出现第三项 `/anthropic-skills:security-foundations`。那是你 Claude 账号里的同一个技能，在 Claude Code 中可以忽略。

示例：

```text
/security-foundations:foundations-check our customer database and its backups
```

### Gemini CLI

```bash
gemini extensions install https://github.com/LYNGMN/security-foundations-plugin
```

重启 Gemini CLI，然后运行 `/foundations-check <要审查的内容>`，或者直接提出安全问题。

### Codex

```bash
git clone --depth 1 https://github.com/LYNGMN/security-foundations-plugin.git
mkdir -p ~/.agents/skills
cp -R security-foundations-plugin/skills/security-foundations ~/.agents/skills/
```

重启 Codex。以后要更新，就在克隆下来的文件夹里运行 `git pull`，再把文件夹复制一遍。

## 它如何思考

这位顾问遵循十条规则。简单来说：

1. **先弄清你有什么。** 对比三类信息：已登记的资产、在网络上实际发现的资产、有保护证明的资产。先补上这些差距，再考虑买新东西。
2. **先做基础，再上新工具。** 打补丁、最小权限、多因素认证、日志留存、经过测试的备份、最新的资产清单，这些放在最前面，并且要有证据。
3. **留下理由。** 记录每项控制措施为什么存在。每个旧系统都要有负责人，并做出决定：淘汰、保留还是替换。
4. **核实供应链。** 要求提供软件物料清单（SBOM）和有签名的构建来源证明。供应商的承诺不算证据。
5. **限制 AI 智能体能做的事。** 给每个智能体定一个自主级别，配上相应的控制措施、一个它自己改不了的紧急停止开关，并且让每个操作都对应到具体的人。
6. **零信任，一步一步来。** 用自动化来做访问决策，不要靠人工设置。
7. **改变行为，而不只是提高意识。** 在人犯错的当下给予指导，衡量上报情况而不是课程完成率，也绝不因为有人没通过钓鱼测试就惩罚他。
8. **出事时先隔离。** 先切断访问，再保全证据，最后才调查。证据保全之前，不要清除数据，也不要重启。
9. **公开透明地赢得信任。** 沟通要快、要讲事实，把事实和猜测分开，绝不隐瞒事件。
10. **对应你的合规义务。** 一套证据应该同时满足 NIST CSF、ISO 27001，以及 ISMS-P、DORA、NIS2 等本地规定。

完整的规则见 [skills/security-foundations/SKILL.md](skills/security-foundations/SKILL.md)。

## 它不会做什么

- 读取密码、`.env` 文件、私钥或其他凭据
- 安装未经验证的软件，或运行破坏性命令
- 编写恶意软件或漏洞利用程序，或帮助绕过身份认证
- 提供法律意见，或认证合规
- 没有证据就说某样东西是安全的，或者编造标准编号

如果它读取的文档或网页里含有针对 AI 的指令，它会把这些指令报告给你，而不会照做。

## 它遵循的标准

| 领域 | 标准 |
|---|---|
| 安全计划 | NIST Cybersecurity Framework (CSF) 2.0 |
| 管理体系 | ISO/IEC 27001:2022 |
| 事件响应 | NIST SP 800-61 Rev. 3 |
| 密码与身份认证 | NIST SP 800-63B Rev. 4 |
| 零信任 | CISA Zero Trust Maturity Model 2.0 |
| 软件供应链 | SLSA v1.2, SBOM (SPDX, CycloneDX), CSAF/VEX |
| AI 智能体 | OWASP Top 10 for Agentic Applications 2026, OWASP Top 10 for LLM 2025, MITRE ATLAS |
| AI 风险 | NIST AI RMF, NIST AI 600-1 |

版本和数量最后核对于 2026 年 10 月。详情见 [standards-map.md](skills/security-foundations/references/standards-map.md)。在审计报告中引用某项标准之前，请再查一遍原始来源。

## 须知

- **它只提建议，不动手。** 它设计计划，检查你的思路。它不会扫描、修改或修复你的系统。
- **不能代替专业人员。** 遇到真实的安全事件，还要联系你的安全团队或事件响应服务商。
- **自定义 GPT 或 Gem 的遵循程度不如技能严格。** 它们只靠粘贴进去的指令运行，所以有时可能会漏掉某个部分。四部分格式和安全规则已经直接写进指令里，以保持输出一致。
- **你的数据留在你的 AI 服务商那里。** 这个项目只提供指令，不会向任何地方发送任何内容。

## 评估结果

2026 年 10 月用 `claude plugin eval` 测得：9 个用例，分别在有技能和没有技能的情况下各运行 3 次（Claude Code 2.1.303，由 Claude Haiku 评分）。

| | 有技能 | 没有技能 |
|---|---|---|
| 平均得分 | **98%** | 51% |
| 该用时用上了技能 | 24 次中 24 次 | — |
| 没有介入与安全无关的问题 | 3 次中 3 次 | — |

差距最大的用例：供应链与智能体安全计划（100% 对 7%）、批准 XDR 采购（100% 对 0%）、无人值守的智能体部署（100% 对 20%）、钓鱼邮件初步响应（93% 对 27%）。

还有两处各漏了一次：一次评分模型没有认可某个钓鱼回答里的 CSF 2.0 映射，一次某个韩语回答被判定负责人写得不够。由模型评分时，每次运行的分数会有些差异。用例在 [evals/](evals/) 里，你可以用下面的命令自己运行。

## 贡献者须知

```text
.claude-plugin/          Claude Code plugin and marketplace manifests
skills/security-foundations/
  SKILL.md               The skill (English, authoritative)
  SKILL.ko.md            Korean mirror for reviewers
  references/            Standards map, failure modes, incident runbook
evals/                   Evaluation cases with graders (claude plugin eval)
commands/                /foundations-check for Claude Code (.md) and Gemini CLI (.toml)
adapters/                ChatGPT kit: instructions (under 8,000 characters) and guide
AGENTS.md, GEMINI.md     Context files for Codex and Gemini CLI
gemini-extension.json    Gemini CLI extension manifest
scripts/                 Validation and packaging
```

在本地验证并构建发布文件（需要 Python 3，无其他依赖）：

```bash
python3 scripts/validate_and_package.py
```

在 Claude Code 中运行评测用例：

```bash
claude plugin eval .
```

欢迎提交 Pull Request。请让 `SKILL.md`、`SKILL.ko.md` 和 `adapters/core-instructions.md` 保持一致，并在发起 PR 之前运行验证脚本。推送与 `.claude-plugin/plugin.json` 中版本号一致的 `v*` 标签后，会自动创建发布版本，发布说明由 GitHub 生成。

如需报告安全问题，请参阅 [SECURITY.md](SECURITY.md)。

## 许可证

[MIT](LICENSE) © 2026 Youngmin
