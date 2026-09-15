# Claude Skills

`claude/skills/` 是 Claude surface（claude.ai Web／Desktop、Cowork、Claude Code）的 Skill Source。與 `chatgpt/skills/` 同名的 Skill 是同一契約的 Claude 移植版；差異只在每個 `SKILL.md` 第 8 行的「Claude port」註記所列項目，其餘逐行相同，`references/` 與 ChatGPT 版 SHA-256 相同。

## 內容（2026-09-15）

| Skill | 來源 | 差異 |
|---|---|---|
| `unknown-pass` | `chatgpt/skills/unknown-pass` @ 0e85a78 | 移除 ChatGPT 專屬交班路由句 |
| `evidence-red-team-reviewer` | `chatgpt/skills/evidence-red-team-reviewer` @ 0e85a78 | 無內容變更 |
| `multi-perspective-reviewer` | `chatgpt/skills/multi-perspective-reviewer` @ 0e85a78 | 無內容變更 |
| `conversation-review` | `chatgpt/skills/conversation-review` @ 0e85a78 | 「邊界」段路由改為 Claude 端規則；步驟 8 設定物件名稱一般化 |
| `write-like-yu-chun` | `chatgpt/skills/write-like-yu-chun` @ 0e85a78 | description 縮至 200 字元（claude.ai 上限），本文無變更 |
| `task-clarification` | 對應 `chatgpt/skills/task-clarification` v1.1（Claude 版 v1.0-claude） | 不重寫提問邏輯；組合 AskUserQuestion → 任務指令 → 授權關卡 → 檔案變更才進 Plan mode |

未移植（Claude 已有等價機制或角色相反）：`claude-handoff`、`thread-handoff`、`work-handoff`。暫緩（部分重疊，待裁定）：`notion-capture`、`project-instruction-designer`、`iterative-work-planner`、`system-design-to-implementation-bridge`。

## 安裝

- claude.ai 帳號層（Web／Desktop／Cowork 共用）：Customize → Skills → Add，上傳以該 Skill 資料夾為根目錄的 zip（含 `references/`）。限制：name ≤ 64 字元、description ≤ 200 字元。
- Claude Code：複製整個資料夾到 `~/.claude/skills/<name>/`（個人）或 repo 的 `.claude/skills/<name>/`（專案）。
- `agents/openai.yaml` 為 ChatGPT／Codex 專用，Claude 不讀取，本目錄不保留。Claude 沒有 `allow_implicit_invocation` 的對應機制，explicit-only 以 description 字句實現。

## 狀態與治理

- GitHub 是 Source；claude.ai 帳號內是否已儲存、載入與觸發行為需另行驗證，Source 不證明 Runtime。
- 治理與版本紀錄在 Notion Skills Registry；Claude surface 的登錄目前以 `[Cowork]` 區塊附註，尚無正式欄位。
- 修改規則同 repo README：read-first、最小完整變更、保留 Git history。同名 Skill 在兩個 surface 各自演進時，在各自的 `SKILL.md` 版本行標明對應關係。
