# Security Foundations instructions kit

For chat tools that cannot load a skill or plugin, such as a Gemini Gem on an account without Gemini skills,
or any assistant with a custom-instructions box.

ChatGPT and Gemini users should install the skill instead:
ChatGPT uses `security-foundations-chatgpt-plugin.zip`, Gemini uses `security-foundations-skill.zip`
(both on the release page).

| File | Where it goes |
|---|---|
| `instructions.md` | Paste the whole file into the instructions box (under 8,000 characters) |
| `knowledge/` (4 files) | Upload all four as knowledge or reference files, if the tool supports them |

## Gemini Gem

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
