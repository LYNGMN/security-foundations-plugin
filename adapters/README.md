# Security Foundations kit for ChatGPT and Gemini

This kit turns ChatGPT or Gemini into the Security Foundations advisor.

| File | Where it goes |
|---|---|
| `instructions.md` | Paste the whole file into the **Instructions** box |
| `knowledge/` (4 files) | Upload all four as **Knowledge** files |

## ChatGPT (custom GPT, paid plan)

1. Open https://chatgpt.com/gpts/editor and select the **Configure** tab.
2. Name: `Security Foundations Advisor`
3. Instructions: paste all of `instructions.md`.
4. Knowledge: upload the four files in `knowledge/`.
5. Capabilities: keep Web Search on.
6. Select **Create** and choose who can see it.

## Gemini (Gem)

1. Open https://gemini.google.com/gems/create
2. Name: `Security Foundations Advisor`
3. Instructions: paste all of `instructions.md`.
4. Knowledge: add the four files in `knowledge/`.
5. Select **Save**.

## Check that it works

Ask: *"An employee opened a phishing attachment and their PC is acting strange. What do we do first?"*
A correct answer has four parts (diagnosis, control table, numbered steps, verification), and tells you to isolate the PC before collecting evidence.

Full guide in your language:
[English](https://github.com/LYNGMN/security-foundations-plugin#readme) ·
[한국어](https://github.com/LYNGMN/security-foundations-plugin/blob/main/README.ko.md) ·
[简体中文](https://github.com/LYNGMN/security-foundations-plugin/blob/main/README.zh-CN.md) ·
[日本語](https://github.com/LYNGMN/security-foundations-plugin/blob/main/README.ja.md)
