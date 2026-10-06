# AI Instructions & Skills

## Repository purpose

This private repository stores the source versions of personally maintained AI instructions and reusable Skills.

The original 14 ChatGPT sources (About Me, Custom Instructions, and 12 Skills) have been imported and are maintained here. The Skills collection now also includes `task-clarification` and `meeting`, bringing the ChatGPT source inventory to 14 Skills. The Codex Custom Instructions file remains a placeholder pending its own source import.

Since 2026-09-16 the repository also holds a Claude surface under `claude/` (see [`claude/README.md`](claude/README.md)): six Skills for claude.ai / Cowork / Claude Code, five of them ports of the ChatGPT Skills with the same exact names, plus a Claude variant of `task-clarification`. Same-named Skills on the two surfaces are the same contract; each `SKILL.md` records its source commit and the specific differences.

Source changes do not install or activate configurations.

## Truth layers

### GitHub

**Source Canonical**

Stores:

- ChatGPT About Me
- ChatGPT Custom Instructions
- ChatGPT Personal Skills (`chatgpt/skills/`)
- Claude Personal Skills (`claude/skills/`)
- Codex Custom Instructions
- future explicitly approved AI instruction sources

### Notion

**Governance / Architecture / Registry Canonical**

Stores:

- architecture
- governance
- Skills Registry
- version status
- testing status
- configuration decisions

Do not duplicate every SKILL.md as a second editable source in Notion.

### AI product UI

**Runtime / Active Configuration Truth**

The configuration actually installed or active in ChatGPT, Codex, or another AI surface must be verified independently.

GitHub source does not prove that the same version is currently installed.

## Change policy

Before changing an existing instruction or Skill:

1. Read the current source.
2. Preserve Git history.
3. Make the smallest complete change.
4. Keep useful project knowledge, safety rules, and permission boundaries.
5. Validate structure and references.
6. Run relevant regression tests when behavior or routing changes.
7. Do not claim performance, speed, or model improvements without testing.
8. Do not assume GitHub source equals currently installed runtime state.

## Source and package maintenance

Maintain each Skill as its complete folder: `SKILL.md` plus any linked `references/`, scripts, or assets. When the product supports Skill packages, import or replace the complete folder/package so supporting references remain available; copying only the entrypoint is insufficient for Skills that link supporting files.

The 2026-09-06 revision targets shared use by Astra and Sol. Five larger Skills route to optional references; short tasks keep essential instructions in the entrypoint. Validation results and installed state are recorded separately in Notion. A source revision or local test does not prove that the ChatGPT desktop installation has been updated or tested.

For future source imports, read the actual configuration or original package. Do not reconstruct source from Notion, Memory, a Registry, or inferred settings. Import the Codex Custom Instructions only when its current source is available.

## Task clarification

[`task-clarification`](chatgpt/skills/task-clarification/SKILL.md) (任務釐清) turns a directionally established request with missing key decisions or specifications into a complete task instruction. Use it only when the user explicitly asks for a clarification-first workflow or selects the skill, not merely because a task is ambiguous. Keep its complete folder, including `agents/openai.yaml`, which preserves the display name and enables implicit skill routing (`allow_implicit_invocation: true`) for matching requests. Existing authorization to execute after clarification carries forward. GitHub storage does not establish ChatGPT installation or product behavior.

The Claude surface variant, [`claude/skills/task-clarification/SKILL.md`](claude/skills/task-clarification/SKILL.md), keeps the same trigger scope and deliverable but composes Claude's built-in AskUserQuestion and Plan mode instead of restating the questioning logic; it carries no `agents/openai.yaml`, so explicit-scope routing is expressed in its description.

## Meeting records

[`meeting`](chatgpt/skills/meeting/SKILL.md)（會議紀錄助手）將使用者提供的逐字稿、草稿或會議資料，整理為繁體中文正式紀錄、精簡版、LINE版、公開版、向上報告、主管版、待辦清單及待確認事項；會議檢視按需執行。只要原始逐字稿時直接交付可用原稿，不套模板、不從摘要反推。

這是一份獨立技能，包含三層可分開維護的規則：

- [會議模板索引](chatgpt/skills/meeting/references/templates.md)：決策、進度回報、腦力激盪、工作規劃／Sprint、檢討回顧、1:1；六份模板各自成檔，含案內格式骨架。
- [正式紀錄外框](chatgpt/skills/meeting/references/formal-format.md)：保留固定主章節及六欄決議／待辦總表，模板只調整各案內容。
- [輸出用途](chatgpt/skills/meeting/references/output-modes.md)與[來源規則](chatgpt/skills/meeting/references/evidence.md)：決定受眾、精簡、公開範圍、事實依據及更正後重產，已交辦不等於已完成。

可用命令：

```text
自動選模板，產生正式紀錄
用進度回報模板，做成LINE版報告，300字內
改用決策模板，重新產生主管版
顯示其他適合的模板
只要逐字稿
```

完整保留 `chatgpt/skills/meeting/`，包含 `references/`、`scripts/`、`agents/`。文字整理不需要Notion或額外安裝其他技能；音訊轉錄取決於執行環境實際可用的工具，機械字數檢查需Python 3。存入GitHub或通過本地檢查，不表示已安裝或啟用於任何產品。

設計參考：[meeting-notes-and-actions](https://github.com/composio-community/awesome-codex-skills/tree/master/meeting-notes-and-actions) 的紀錄／待辦流程、[meeting-insights-analyzer](https://github.com/composio-community/awesome-codex-skills/tree/master/meeting-insights-analyzer) 的來源舉證及選用檢視、[notion-meeting-intelligence](https://github.com/composio-community/awesome-codex-skills/tree/master/notion-meeting-intelligence) 的六種會議分類。本版依使用者要求重寫為會後整理規則；三者是設計參考，不是執行依賴。
