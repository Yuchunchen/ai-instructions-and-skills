# Claude Skills

`claude/skills/` 是 Claude surface（claude.ai Web／Desktop，含原 Cowork 代理工作；Claude Code）的 Skill Source。與 `chatgpt/skills/` 同名的 Skill 是同一契約的 Claude 移植版；差異只在每個 `SKILL.md` 第 8 行的「Claude port」註記所列項目，其餘逐行相同，`references/` 與 ChatGPT 版 SHA-256 相同。

## 內容（2026-09-15；2026-10-11 增補）

| Skill | 來源 | 差異 |
|---|---|---|
| `unknown-pass` | `chatgpt/skills/unknown-pass` @ 0e85a78 | 移除 ChatGPT 專屬交班路由句 |
| `evidence-red-team-reviewer` | `chatgpt/skills/evidence-red-team-reviewer` @ 0e85a78 | 無內容變更 |
| `multi-perspective-reviewer` | `chatgpt/skills/multi-perspective-reviewer` @ 0e85a78 | 無內容變更 |
| `conversation-review` | `chatgpt/skills/conversation-review` @ 0e85a78 | 「邊界」段路由改為 Claude 端規則；步驟 8 設定物件名稱一般化 |
| `write-like-yu-chun` | `chatgpt/skills/write-like-yu-chun` @ ff24abe（v1.5.0，2026-10-11 重新移植；前版 v1.3 @ 0e85a78） | 無內容變更；description 恢復完整版；含 `references/`、`evals/` |
| `task-clarification` | 對應 `chatgpt/skills/task-clarification` @ 6f1d9f1（2026-09-16 concise workflow；Claude 版 v1.0-claude） | 不重寫提問邏輯；組合 AskUserQuestion → 任務指令 → 授權關卡 → 檔案變更才進 Plan mode。ChatGPT 版以 `agents/openai.yaml` 做 intent-scoped implicit routing，Claude 版以 description 表達同一觸發範圍 |
| `iterative-work-planner` | `chatgpt/skills/iterative-work-planner` @ d0064e8（v1.0，2026-10-11 移植） | 補 Claude 寫入 Notion 工作狀態的最小規則（含 `last_writer`）；移除 ChatGPT handoff 路由；references 相同 |

未移植（Claude 已有等價機制或角色相反）：`claude-handoff`、`thread-handoff`、`work-handoff`。暫緩（部分重疊，待裁定）：`notion-capture`、`project-instruction-designer`、`system-design-to-implementation-bridge`。`iterative-work-planner` 已於 2026-10-11 移植，承接跨 AI 主線（`cross-ai-resumable-workflow`）的 Claude 端寫入。

## 安裝

- claude.ai 帳號層（Web／Desktop 共用，含原 Cowork 代理工作）：Customize → Skills → Add，上傳以該 Skill 資料夾為根目錄的 zip（含 `references/`）。限制：name ≤ 64 字元；description 依 2026-10-11 查核的官方文件為 ≤ 1,024 字元（Agent Skills 規格；先前記錄的 200 字元為舊限制，`write-like-yu-chun` 已於 2026-10-11 恢復完整 description）。2026-10-05 起 zip 上傳會保留 `references/` 等附檔。
- Claude Code：複製整個資料夾到 `~/.claude/skills/<name>/`（個人）或 repo 的 `.claude/skills/<name>/`（專案）。
- **Plugin 自動同步（2026-10-11 起）**：`claude/` 同時是 plugin `yc-skills` 的根目錄（`claude/.claude-plugin/plugin.json`），repo 根目錄的 `.claude-plugin/marketplace.json` 為私有 marketplace `yc-ai-skills`。
  - claude.ai 組織：Owner 在 Organization settings → Plugins & skills → Add → Sync from GitHub 選本 repo，開啟 Sync automatically；之後推送到 `main` 即同步。
  - Claude Code：`/plugin install yc-skills --marketplace Yuchunchen/ai-instructions-and-skills`。
  - `plugin.json` 刻意不設 `version`，讓安裝端依 commit 追蹤更新；validate 會提示缺 version，屬預期。
  - Plugin 內的 skill 名稱帶前綴（`yc-skills:<name>`）。確認同步版可用後，再停用先前手動上傳的同名 skill，避免同一 skill 出現兩份。
  - 合併到 `main` 就會發佈到組織；修改仍須經 PR。
- `agents/openai.yaml` 為 ChatGPT／Codex 專用，Claude 不讀取，本目錄不保留。Claude 沒有 `allow_implicit_invocation` 的對應機制，explicit-only 以 description 字句實現。

## 狀態與治理

- 2026-09-16：PR #1 已 merge 至 `main`（merge commit 748d345）；本目錄自此為 Claude surface 的正式 Source。
- 2026-10-11：Claude session 讀取組織層 6 件 skill，內容與本目錄一致（僅檔尾換行差異），references 齊全。
- 2026-09-16：六件已出現在 claude.ai 帳號的 skill 清單（Cowork session 工具清單可見），視為「帳號已儲存」；自動觸發與 references 載入行為仍未測。
- GitHub 是 Source；claude.ai 帳號內是否已儲存、載入與觸發行為需另行驗證，Source 不證明 Runtime。
- 治理與版本紀錄在 Notion Skills Registry；Claude surface 的登錄目前以 `[Cowork]` 區塊附註，尚無正式欄位。
- 修改規則同 repo README：read-first、最小完整變更、保留 Git history。同名 Skill 在兩個 surface 各自演進時，在各自的 `SKILL.md` 版本行標明對應關係。
