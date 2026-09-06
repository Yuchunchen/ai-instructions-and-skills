# Claude Handoff

**版本：v1.1｜2026-07-19**

產生供 Claude 或 Claude Cowork 接手的安全任務契約。重點不只是摘要，而是明確界定應做、不應做、核准點、可修改範圍與驗證要求。

## 基本原則

- 只使用目前可見對話、使用者提供資料，以及工具實際讀取到的內容。
- 不假裝 Claude 能讀取本討論串、未提供附件、Notion 或其他系統。
- 清楚區分事實、決策、暫定方向、建議、已完成、進行中、尚未開始與待確認。
- 不把候選方案寫成已核准決策。
- 不把預計執行的內容寫成已完成。
- 不補造日期、數字、版本、檔名、責任人、來源或完成狀態。
- 資訊矛盾時保留差異並標示待釐清。
- 保留 canonical 邊界、被否決方案、版本、風險與回復要求。
- 使用使用者主要語言；中文時使用繁體中文與台灣用語。
- 使用手機友善 Markdown，不使用表格或過深縮排。

## 處理流程

1. 說明 Claude 要接手的工作與預期成果。
2. 建立最小充分背景與目前狀態。
3. 抽取正式決策、適用範圍與可調整程度。
4. 列出 Claude 應做與不應做。
5. 判斷是否需要 implementation plan。
6. 標示 canonical、Notion、檔案與程式的修改邊界。
7. 列出來源與 Claude 的可存取性。
8. 定義驗證、變更紀錄、回復方式與核准節點。
9. 若涉及 AI 設定／Skills／surface 變更，建立 Configuration / Surface Delta：實際 UI 狀態、舊新差異、受影響頁面、需要的最小 canonical patch 與不應複製的 SOP。
10. 整理應帶回長期系統的 Knowledge Delta。
11. 加入 Claude 起始指令。

## Implementation Plan 啟動條件

涉及下列任一事項時，要求 Claude 先提出 implementation plan，未經確認不要直接執行：

- 程式或自動化
- 批次檢查或批次改寫
- 檔案搬移、刪除、重新命名
- Notion 或 Dropbox 的系統性調整
- INDEX.md、CLAUDE.md、Architecture、Registry 或 canonical
- 系統規格、資料模型、工作流、權限或正式文件的變更

Implementation plan 至少包含：

1. 目標與成功條件
2. 影響範圍
3. 預計修改項目
4. 執行順序
5. 驗證方式
6. 回復方式
7. 需使用者確認的節點

要求 Claude：

- read-first
- 未經確認不直接修改 canonical
- 修改前呈現預計變更或 diff
- 若偏離原計畫，留下 implementation notes、working notes 或 deviations
- 完成後提供變更清單、驗證結果與未解問題

## 固定輸出

[ChatGPT-Delta｜for Claude]

### 1. 交班目的
說明 Claude 要接手什麼，以及預期產出。

### 2. 核心背景
提供 Claude 理解任務所需的最小充分背景。

### 3. 目前狀態
分為：
- 已確認事實
- 已完成成果
- 目前進行中
- 尚未開始

### 4. 已形成決策
列出正式決策、理由、適用範圍與是否可調整。若沒有，寫「目前尚無正式定案」。

### 5. 重要前提與限制
列出政策、權限、時間、資源、格式、版本、使用者要求、canonical 邊界與風險。

### 6. Claude 應做
依優先順序列出任務、所需輸入、預期產出、成功條件、是否需先詢問使用者，以及是否需要 implementation plan。

### 7. Claude 不應做
至少檢查：
- 不重做已完成項目
- 不把建議當成決策
- 不自行擴張範圍
- 不假裝已讀取未提供的資料
- 不未經同意改寫 canonical
- 不任意更改名詞、版本或責任分工
- 不為完整性而過度工程化
- 不自行新增不必要的 Agent、Registry、Skill 或自動化

### 8. Configuration / Surface Delta
若變更涉及 About Me、Global Custom Instructions、Project Instructions、Skills、Apps、模型／模式或 AI surface，必須列出：
- 哪項設定或能力已實際變更
- UI 是否已確認生效
- 舊做法與新做法
- 受影響的 Architecture、AI surface、Setup Log、instruction snapshot、Skills manifest 或教學內容
- 建議的最小 canonical patch
- 哪些 SOP 應留在 Skill，不應複製進 Architecture
若無，寫「本次無設定或 surface 變更」。

### 9. Implementation Plan 要求
列出本次是否需要 plan，以及必須包含的項目。若不需要，寫「本次不需要 implementation plan」。

### 10. 尚待確認
只列會改變方向、研究設計、系統架構或執行方式的重要未知。

### 11. 防 drift 與 canonical 邊界
說明應延續、不應重做、不應擴張、不得自行假設及不可直接修改的內容。

### 12. 參考資料與可存取性
將每項資料標示為：
- 已包含於交班稿
- Claude 需重新取得
- 使用者需重新上傳
- 只有名稱，尚未驗證

### 13. Knowledge Delta
列出新決策、新發現、新限制、被修正的假設、新任務、新風險、建議寫回位置、不應覆寫內容與尚需確認事項。

### 14. Claude 起始指令
固定加入：

「請先依本交班稿重建目前狀態，不要重做已完成項目，也不要假設能存取未提供的來源。先檢查『尚待確認』是否有會改變架構的問題；若沒有，從『Claude 應做』第 1 項開始。涉及系統、程式、Notion 或檔案修改時，先提出 implementation plan，未經確認不得直接改動 canonical。」

## 邊界

- 本 Skill 只產生交班契約，不直接修改 Architecture、INDEX.md、CLAUDE.md、Registry 或 canonical。
- 使用者另要求把已確認 Knowledge Delta 寫入 Notion 時，可同時使用 `notion-capture`。
- Global Instructions、About Me、Project Instructions 或 Skills 變更若影響現行工作流，應要求 Claude 同步檢查 Architecture、AI surface、Setup Log 與 instruction snapshot；不得只更新其中一處。
- 若只是換到新 ChatGPT 討論串，使用 `thread-handoff`。
