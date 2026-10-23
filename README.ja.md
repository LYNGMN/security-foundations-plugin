# Security Foundations

[English](README.md) · [한국어](README.ko.md) · [简体中文](README.zh-CN.md) · **日本語**

[![Release](https://img.shields.io/github/v/release/LYNGMN/security-foundations-plugin)](https://github.com/LYNGMN/security-foundations-plugin/releases/latest)
[![Validate](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml/badge.svg)](https://github.com/LYNGMN/security-foundations-plugin/actions/workflows/validate.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

AI アシスタントに加えられる、セキュリティの相談役です。セキュリティの疑問を普通の言葉で聞くだけで、経験豊富なセキュリティ責任者のように答えます。まず、あなたが何を持っているのかを確かめます。そのうえで、実行して確認できる計画を示します。

**Claude**（アプリと Claude Code）、**ChatGPT**、**Gemini**（Web と CLI）、**Codex** で使えます。あなたが書いた言語で答えます。

## できること

回答はいつも同じ4つの部分でまとまっています。そのまま同僚や監査担当者に渡せます。

| 部分 | わかること |
|---|---|
| 1. 資産と盲点の診断 | 何を持っているか、誰の管理下にもないものは何か、守られていると証明できないものは何か |
| 2. 対策の計画 | 何を導入すべきか。層ごとに、根拠となる基準と運用への負担を添えて示します |
| 3. 手順書 | 今日から誰でも実行できる、番号付きの作業 |
| 4. 検証と残るリスク | 各対策が効いているかの確かめ方と、まだ無防備な部分 |

こんな質問を試してみてください。

- *「社員がフィッシングメールの添付ファイルを開いてしまい、PC の様子がおかしいです。まず何をすべきですか？」*
- *「AI エージェントや MCP サーバーを社内システムにつなぎたいです。安全の枠組みと承認の手順を設計してください。」*
- *「古いシステムと外部ベンダーのパッチ適用を点検して、何から直すべきか教えてください。」*
- *「実際に悪用されている脆弱性の重要な修正パッチが出ました。サプライチェーンのリスクを考えて、1週間待つべきでしょうか？」*
- *「ISO 27001 の取得を準備しています。いちばん大きな不足はどこですか？」*

IT・セキュリティ担当チーム、開発者、起業家、セキュリティ専門家がいない小さなチームの管理者、監査の準備をしている方のためのものです。

## インストール

すでに使っている AI の場所を選んでください。最初の3つはプログラミングが不要です。

| 使っているもの | 所要時間 | 移動先 |
|---|---|---|
| Claude アプリ（Web、デスクトップ、モバイル） | 2分 | [Claude アプリ](#claude-app) |
| ChatGPT | 5分 | [ChatGPT](#chatgpt) |
| Gemini（Web） | 5分 | [Gemini](#gemini) |
| Claude Code | 1分 | [Claude Code](#claude-code) |
| Gemini CLI | 1分 | [Gemini CLI](#gemini-cli) |
| Codex | 1分 | [Codex](#codex) |

### Claude app

Claude の有料プランで、コード実行をオンにしている必要があります。

1. [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip) をダウンロードします。解凍しないでください。
2. Claude で **Settings → Capabilities**（設定 → 機能）を開きます。
3. **Skills**（スキル）で **Upload skill**（スキルをアップロード）を選び、ダウンロードしたファイルを指定します。
4. スキルがオンになっていることを確かめます。そのあと、どのチャットでもセキュリティの質問をしてみてください。質問に合うときは、Claude が自分でスキルを使います。

### ChatGPT

GPT を作るには、ChatGPT の有料プランが必要です。

1. [**security-foundations-chatgpt-kit.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-chatgpt-kit.zip) をダウンロードして解凍します。
2. [chatgpt.com/gpts/editor](https://chatgpt.com/gpts/editor) を開き、**Configure**（構成）タブを選びます。
3. **Name**（名前）：`Security Foundations Advisor`
4. **Description**（説明）：`セキュリティの状態を基礎から診断し、根拠にもとづく対策計画をつくります。`
5. **Instructions**（指示）：キットの `instructions.md` を開き、すべてコピーして貼り付けます。
6. **Conversation starters**（会話のきっかけ）：[できること](#できること)にある質問から、2～3個をコピーします。
7. **Knowledge**（ナレッジ）：キットの `knowledge` フォルダにある4つのファイルをアップロードします。
8. **Capabilities**（機能）：Web Search（Web 検索）はオンのままにします。ほかは不要です。
9. **Create**（作成）を選びます。共有したい場合を除いて、**Only me**（自分のみ）を選んでください。

### Gemini

Gemini では Gem に代わってスキルが使われるようになりました。Gemini の Web 版と Mac 版アプリで使えます。

1. [**security-foundations-skill.zip**](https://github.com/LYNGMN/security-foundations-plugin/releases/latest/download/security-foundations-skill.zip) をダウンロードして解凍します。`security-foundations` というフォルダができます。
2. [gemini.google.com](https://gemini.google.com) を開き、**Settings → Skills**（設定 → スキル）に進みます。
3. スキルの読み込みを選び、フォルダ内の `SKILL.md` を選択します。
4. おすすめ：新しいスキルにカーソルを合わせ、**Skill actions → Replace skill**（スキルの操作 → スキルを置き換え）を選んで、`security-foundations` フォルダごと選びます。参考ファイルも一緒に入ります。
5. チャットで `/security-foundations` と入力するか、そのままセキュリティの質問をします。内容が合えば Gemini が自動でスキルを使います。

まだスキル機能がないアカウントでは、[ChatGPT 用キット](#chatgpt)を使って [gemini.google.com/gems/create](https://gemini.google.com/gems/create) で Gem を作ってください。`instructions.md` を貼り付け、`knowledge` の4つのファイルを追加します。

### Claude Code

Claude Code に次の2行を入力します。

```text
/plugin marketplace add LYNGMN/security-foundations-plugin
/plugin install security-foundations@security-foundations-marketplace
```

新しいセッションを開くと、`/` メニューに2つの項目が出ます。

| 項目 | 使う場面 |
|---|---|
| `/security-foundations:foundations-check` | **最初はこちら。** 点検したい対象を続けて書きます。何も書かずに実行すると、範囲を確かめる質問から始めます。 |
| `/security-foundations:security-foundations` | ふだんは不要です。普通の言葉でセキュリティの質問をすれば自動で使われます。自動で使われなかったときだけ直接呼び出します。 |

Claude アプリにもスキルをアップロードしている場合、デスクトップアプリには3つ目の `/anthropic-skills:security-foundations` が出ることがあります。Claude アカウントにある同じスキルなので、Claude Code では無視してかまいません。

例：

```text
/security-foundations:foundations-check our customer database and its backups
```

### Gemini CLI

```bash
gemini extensions install https://github.com/LYNGMN/security-foundations-plugin
```

Gemini CLI を再起動し、`/foundations-check <what to review>` を実行します。ふつうにセキュリティの質問をするだけでも使えます。

### Codex

```bash
git clone --depth 1 https://github.com/LYNGMN/security-foundations-plugin.git
mkdir -p ~/.agents/skills
cp -R security-foundations-plugin/skills/security-foundations ~/.agents/skills/
```

Codex を再起動します。あとで更新するときは、クローンしたフォルダで `git pull` を実行し、もう一度フォルダをコピーします。

## 考え方

このアドバイザーは10のルールに従います。かんたんにまとめると、次のとおりです。

1. **まず、持っているものを知る。** 登録されているもの、ネットワークで実際に見つかるもの、守られている証拠があるものを比べます。何かを買う前に、そのずれを埋めます。
2. **新しい道具より、基本が先。** パッチ適用、最小権限、多要素認証、ログの保存、テスト済みのバックアップ、最新の資産一覧を、証拠つきで最優先にします。
3. **理由を残す。** それぞれの対策がなぜあるのかを記録します。古いシステムには、すべて担当者と「廃止・維持・置き換え」の判断を決めます。
4. **サプライチェーンを確かめる。** ソフトウェア部品表（SBOM）と、署名つきのビルド来歴を求めます。ベンダーの約束は証拠ではありません。
5. **AI エージェントにできることを限る。** エージェントごとに自律の段階を決め、それに合う対策、自分では書き換えられない緊急停止の仕組み、実在の人に結びついた操作を用意します。
6. **ゼロトラストは少しずつ。** 手作業の設定に頼らず、アクセスの判断を自動化します。
7. **意識だけでなく、行動を変える。** ミスをしたその場で教え、研修の修了ではなく報告の数を測り、フィッシング訓練に失敗した人を罰しません。
8. **インシデントでは、まず隔離。** アクセスを断ち、次に証拠を保全し、そのあとで調べます。証拠を残す前に、消去や再起動をしてはいけません。
9. **信頼は公開の場で築く。** すばやく事実にもとづいて伝え、事実と推測を分け、インシデントを隠しません。
10. **自分の義務に結びつける。** 1組の証拠で、NIST CSF、ISO 27001、ISMS-P、DORA、NIS2 などの各国・各地域の規則に応えられるようにします。

ルールの全文は [skills/security-foundations/SKILL.md](skills/security-foundations/SKILL.md) にあります。

## やらないこと

- パスワード、`.env` ファイル、秘密鍵などの認証情報を読むこと
- 検証されていないソフトウェアを入れたり、破壊的なコマンドを実行したりすること
- マルウェアやエクスプロイトを書くこと、認証を回避する手助けをすること
- 法的な意見を述べたり、コンプライアンスを認証したりすること
- 証拠なしに「安全です」と言うこと、標準の番号をでっち上げること

読み込んだ文書や Web ページに AI あての指示が書かれていても、従いません。その指示があったことを報告します。

## 準拠する標準

| 分野 | 標準 |
|---|---|
| セキュリティプログラム | NIST Cybersecurity Framework (CSF) 2.0 |
| マネジメントシステム | ISO/IEC 27001:2022 |
| インシデント対応 | NIST SP 800-61 Rev. 3 |
| パスワードと認証 | NIST SP 800-63B Rev. 4 |
| ゼロトラスト | CISA Zero Trust Maturity Model 2.0 |
| ソフトウェアサプライチェーン | SLSA v1.2, SBOM (SPDX, CycloneDX), CSAF/VEX |
| AI エージェント | OWASP Top 10 for Agentic Applications 2026, OWASP Top 10 for LLM 2025, MITRE ATLAS |
| AI リスク | NIST AI RMF, NIST AI 600-1 |

バージョンと件数は、2026年10月に最後に確認しました。詳しくは [standards-map.md](skills/security-foundations/references/standards-map.md) を見てください。監査報告書で標準を引用する前には、必ず原典をもう一度確かめてください。

## 知っておいてほしいこと

- **助言はしますが、実行はしません。** 計画を設計し、あなたの考えを点検します。システムのスキャン、変更、修正はしません。
- **専門家の代わりにはなりません。** 実際にインシデントが起きたときは、社内のセキュリティチームやインシデント対応の事業者にも連絡してください。
- **GPT や Gem は、スキルほど厳密には従いません。** 貼り付けた指示だけに頼るため、ときどき一部を飛ばすことがあります。そのため、4つの部分の形式と安全のルールは指示の本文に直接書いてあります。
- **データは AI の提供元のもとにとどまります。** このプロジェクトが加えるのは指示だけです。どこにも何も送りません。

## 評価結果

2026年10月に `claude plugin eval` で測定しました。9つのケースを、スキルありとスキルなしでそれぞれ3回ずつ実行しています（Claude Code 2.1.303、採点は Claude Haiku）。

| | スキルあり | スキルなし |
|---|---|---|
| 平均スコア | **98%** | 51% |
| 使うべき場面でスキルが使われた回数 | 24回中24回 | — |
| セキュリティと関係ない質問に割り込まなかった回数 | 3回中3回 | — |

差が大きかったのは、サプライチェーンとエージェントの計画（100% 対 7%）、XDR 購入の承認依頼（100% 対 0%）、無人で本番に出すエージェント（100% 対 20%）、フィッシングの初動対応（93% 対 27%）です。

1回ずつ取りこぼしたところが2つ残っています。フィッシングの回答1つで採点モデルが CSF 2.0 の対応づけを認めず、韓国語の回答1つは担当者の指定が足りないと判定されました。モデルが採点するため、スコアは実行ごとに少し変わります。ケースは [evals/](evals/) にあり、下のコマンドで自分でも実行できます。

## 開発に参加する方へ

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

ローカルで検証し、リリース用のファイルをビルドします（Python 3 が必要で、ほかの依存はありません）。

```bash
python3 scripts/validate_and_package.py
```

Claude Code で評価ケースを実行します。

```bash
claude plugin eval .
```

プルリクエストを歓迎します。`SKILL.md`、`SKILL.ko.md`、`adapters/core-instructions.md` の内容をそろえ、PR を出す前に検証スクリプトを実行してください。リリースは、`.claude-plugin/plugin.json` のバージョンに合う `v*` タグをプッシュすると自動で作られます。リリースノートは GitHub が生成します。

セキュリティ上の問題を報告するときは、[SECURITY.md](SECURITY.md) を見てください。

## ライセンス

[MIT](LICENSE) © 2026 Youngmin
