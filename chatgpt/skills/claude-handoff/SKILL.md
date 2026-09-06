---
name: claude-handoff
description: "在已確認由 Claude Chat、Project、Cowork 或 Code 接手時，整理任務背景、既有授權、成果與驗證要求。涉及 Notion、程式或設定變更本身不構成觸發條件。"
---

# Claude Handoff

**版本：v1.3｜2026-09-06**

產生供 Claude、Claude Cowork 或 Claude Code 接手的安全任務契約。重點不只是摘要，而是明確界定應做、不應做、核准點、可修改範圍與驗證要求。

## 使用時機

- 使用者明確要求交給 Claude，或已確認由 Claude 承接長文件整合、程式工作或獨立第二意見，而且需要傳遞任務脈絡。
- 不因涉及 Notion、Architecture、Registry 或正式文件就自動使用本 Skill。日常 Notion 維護預設由 ChatGPT Work 承接；Claude 也可在授權範圍內更新其主責工作的對應頁面。
- 獨立第二意見只交付審查結果，除非另有修改授權；不將它設為所有工作的必經核准。

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

## Implementation Plan 與既有授權

交班必須帶入使用者已授權的工作、可修改範圍、尚未涵蓋的動作與真正的核准點。只因涉及程式、批次唯讀檢查、Notion 或正式文件，不要求重新提出計畫等待批准。

- 單一明確修正或唯讀查核：接手者讀取必要現況後，直接完成已授權工作與相關驗證。
- 多步驟、跨系統或影響較大的變更：準備最小充分 plan，列目標、影響範圍、執行順序、驗證與適用的回復方式；已有 plan 與授權可沿用。
- 只有新增範圍、未授權的外部動作、不可逆風險或正式權責規定才要求新核准。需要新核准時，先把可完成的準備與具體變更整理好，再停在真正的批准邊界。
- 修改目標前讀取現況；適用的 Dropbox／INDEX.md／CLAUDE.md／SYSTEM.Exec 專案規則仍保留，不以一般交班契約覆蓋專屬檔案操作要求。
- 完成後回報實際變更、驗證結果、未解問題與必要回復資訊。偏離原範圍要說明，不以交班推定擴權。

## 輸出方式

保留標記 [ChatGPT-Delta｜for Claude]。短任務用精簡版：任務與成果、必要背景／目前狀態、既有授權與限制、可取得來源、下一步與驗證、起始指令。下列是較完整情境的欄位選單，可合併或省略不相關章節，不必填「無」湊齊格式。重要授權、限制、來源可存取性與狀態差異不可因精簡而消失。

## 完整情境參考格式

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
列出本次是否需要 plan，以及必須包含的項目。不需要時省略此節。

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
依本次授權調整後加入：

「請先依本交班稿重建目前狀態，不要重做已完成項目，也不要假設能存取未提供的來源。先檢查『尚待確認』是否有會改變架構的問題；若沒有，從『Claude 應做』第 1 項開始。沿用交班中已確認的授權與計畫，完成對應工作及驗證；只有新增範圍、未授權動作或正式權責規定才請求新核准。遇到實際阻塞時，說明已完成部分與解除條件，繼續可獨立完成的工作。」

## 邊界

- 本 Skill 只產生交班契約，不直接修改 Architecture、INDEX.md、CLAUDE.md、Registry 或 canonical。
- 使用者另要求把已確認 Knowledge Delta 寫入 Notion 時，可同時使用 `notion-capture`。
- Claude 接手的 Global Instructions、About Me、Project Instructions 或 Skills 變更若影響現行工作流，依變更範圍檢查相關 Architecture、AI surface、Setup Log 與 instruction snapshot，只更新實際受影響的頁面。Claude 可直接更新其已授權主責工作的對應 Notion 頁面，完成後回讀並回報；其他 AI 接手時先讀最新版。
- 若只是換到新 ChatGPT 討論串，使用 `thread-handoff`。

## 完成與失敗處理

交班稿能讓 Claude 在不讀舊對話的情況下開始指定工作，且成果、授權、來源與驗證條件清楚，即完成交班。產生契約不等於 Claude 已接收、已執行或已更新系統。
來源不可存取時附必要摘要並標示重新取得方式；關鍵資料不足時指出受阻任務，其餘可接續事項保留。不用格式完整度掩蓋未知。
