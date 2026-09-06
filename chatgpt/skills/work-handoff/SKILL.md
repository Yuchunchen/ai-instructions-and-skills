---
name: work-handoff
description: "將目前可見工作整理成中立、可重用的標準交班核心，適用於使用者只說「幫我交班」、尚未決定交給 ChatGPT 或 Claude、需要同時交給多個目的地，或要求先建立標準 handoff core。若接手者已明確是新 ChatGPT、Claude 或 Notion，優先搭配對應的 thread-handoff、claude-handoff 或 notion-capture。"
---

# Work Handoff Core

**版本：v1.1｜2026-07-19**

建立不綁定特定接手者的標準交班核心，供後續轉換為 ChatGPT、Claude 或 Knowledge Delta 版本。

## 基本原則

- 只使用目前可見對話、使用者提供資料，以及工具實際讀取到的內容。
- 不假裝能讀取其他討論串、未提供附件、Notion 或其他 AI 的記憶。
- 交班核心必須能脫離原討論獨立閱讀。
- 區分事實、決策、暫定方向、建議、已完成、進行中、尚未開始與待確認。
- 不補造日期、數字、版本、檔名、責任人、來源或完成狀態。
- 資訊矛盾時保留矛盾並標示待釐清。
- 保留決策理由、限制、來源可存取性、風險與被否決方案。
- 使用使用者主要語言；中文時使用繁體中文與台灣用語。
- 預設使用手機友善 Markdown，不使用表格。

## 處理流程

1. 辨識交班目的，但不要自行假定接手者。
2. 建立最小充分背景。
3. 抽取已形成決策與理由。
4. 整理目前狀態及可確認的完成成果。
5. 列出下一步、完成條件與重要未知。
6. 標示資料是否已包含、需重新取得或需重新上傳。
7. 設定防 drift 邊界。
8. 若任務涉及 About Me、Global Custom Instructions、Project Instructions、Skills 或 AI surface，列出 Configuration / Workflow Delta 與需同步的頁面。
9. 列出 Knowledge Delta 候選，但不要自動寫入 Notion。
10. 若接手者不明且會影響格式，只問一次：
   「這份交班要給新的 ChatGPT 討論串、Claude，還是先保留為中立交班核心？」
11. 若使用者要求不要詢問，直接輸出中立核心。

## 固定輸出

[Work-Handoff-Core]

### 1. 交班目標
說明要接續什麼工作，以及預期達成什麼。

### 2. 核心背景
提供接手者理解任務所需的最小充分背景。

### 3. 目前狀態
分為已確認事實、已完成、進行中與尚未開始。

### 4. 已形成決策
列出決策、理由與適用範圍。沒有正式定案時明確說明。

### 5. 暫定方向與假設
列出尚未核准、尚待驗證或只是工作假設的內容。

### 6. 重要限制
包括政策、格式、資源、時間、權限、版本與使用者要求。

### 7. 已有成果與參考資料
列出成果、檔案、圖片、頁面、來源，以及接手者是否可直接取得。

### 8. 下一步
依優先順序列出動作、所需輸入、預期產出與完成條件。

### 9. 尚待確認
只列會改變方向、架構或執行方式的重要未知。

### 10. 風險與失敗點
指出最可能造成錯誤、延誤、誤解或重工的地方。

### 11. 防 drift 邊界
說明應延續、不應重做、不應擴張與不得自行假設的內容。

### 12. Configuration / Workflow Delta
若涉及 AI 設定或工作流變更，列出：變更物件、UI 狀態、舊新差異、受影響的 Architecture／AI surface／Setup Log／instruction snapshot／Skills，以及應由誰更新。若無，寫「本次無設定或工作流變更」。

### 13. Knowledge Delta 候選
列出可能值得長期沉澱的新決策、新方法、新限制、新修正與新風險。

### 14. 目的地轉換提示
說明下一步適合轉成：
- `[ChatGPT-Handoff]`
- `[ChatGPT-Delta｜for Claude]`
- Notion Knowledge Delta
或維持中立核心。

## 邊界

- 不直接寫入 Notion。
- 不替 Claude 建立詳細 implementation plan。
- 不把完整交班核心當成正式 Knowledge Delta。
- 接手者明確時，優先使用目的地專屬 Skill。
