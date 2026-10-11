# 規劃情境範例

本檔供相關情境按需查閱。依 SKILL.md 已選模式、實際風險與使用者要求挑選段落；沒有相關問題時可明說未發現，不為數量或格式新增問題、產物或核准。範例中的工具、角色與專案條件不自動套用到當前任務。

# 使用範例一｜健康台灣深耕計畫 POS

使用者：

「POS 的實作架構已經確認，請拆成一週內可執行的工作計畫。」

正確行為：

將已確認的 POS Implementation Plan 拆成：

### Phase 1｜工作環境與責任確認

任務可能包括：

* 確認三個 Thread 的功能。
* 確認兩份正式主稿位置。
* 指派計畫書一與計畫書二的彙整 Owner。
* 確認 ChatGPT–Claude Handoff 格式。

Approval Gate：

* 總主持人核定 Thread 與正式版本架構。

### Phase 2｜計畫架構與核心工作包凍結

任務可能包括：

* 確認計畫書一區域問題。
* 凍結三至五個核心工作包。
* 確認計畫書二亮點與工作包。
* 將定案內容交給 Claude 更新。

Approval Gate：

* 總主持人核定兩案工作包。

### Phase 3｜模組內容與證據

任務可能包括：

* 各模組 Owner 提供流程與基線。
* ChatGPT協助建立因果鏈。
* Claude 整合正式主稿。

Checkpoint：

* 每個工作包均有 Problem、Intervention、KPI、Budget、Outcome 與 Sustainability。

### Phase 4｜KPI、預算與紅隊

任務可能包括：

* 主計室確認可編列性。
* ChatGPT進行紅隊。
* Claude完成一致性整合。

### Phase 5｜定稿

Approval Gate：

* 總主持人核定正式送件版。

不要重新討論是否需要一週作戰板，也不要重新改變三院節點定位。

---

# 使用範例二｜Notion Architecture 更新

使用者：

「Implementation Bridge 已決定要更新 Notion Architecture、INDEX 與 Skills Registry，請拆成工作計畫。」

正確行為：

拆分為：

1. 盤點現況。
2. 建立修改清單。
3. 指定當次主責 AI：Notion 日常維護預設 ChatGPT Work；INDEX 檔案操作另依適用專案流程。
4. 主責 AI 準備 Implementation Plan；只有確實由 Claude 接手的部分才產生 Claude Handoff。
5. 取得尚未涵蓋的必要範圍與重大變更核准。
6. 由已授權主責 AI 執行對應修改。
7. 回讀頁面／檔案，驗證內容、連結與版本。
8. 更新 Setup Log。
9. 完成交班。

以下核准僅在既有授權尚未涵蓋時需要：

* 使用者核准修改範圍。
* 使用者核准重大 Architecture 變更。

只有實際寫入並回讀驗證後，主責 AI 才能宣稱已修改 Notion；僅產生計畫時不得宣稱已完成。

---

# 使用範例三｜自動化系統

使用者：

「人工 Pilot 已完成，現在要把流程交給 Codex 建立自動化。」

正確行為：

階段可包括：

1. 確認自動化需求與邊界。
2. 建立測試資料與測試環境。
3. Codex 開發最小版本。
4. 技術測試。
5. 使用者驗收。
6. 小規模上線。
7. 監測與回復演練。
8. 正式啟用。

Approval Gates：

* 技術規格核准。
* 上線核准。
* 正式啟用核准。

Dependencies：

* 權限。
* 測試資料。
* API 或系統介面。
* 回復機制。

不要在本 Skill 內直接撰寫完整程式。
