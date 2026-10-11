# 任務、依賴與迭代參考

本檔供相關情境按需查閱。依 SKILL.md 已選模式、實際風險與使用者要求挑選段落；沒有相關問題時可明說未發現，不為數量或格式新增問題、產物或核准。範例中的工具、角色與專案條件不自動套用到當前任務。

## 導覽

- [可恢復工作狀態](#可恢復工作狀態)：主線、分支、checkpoint 與部分成功。
- [重要定義](#重要定義)：Phase、Task、Owner、依賴、檢查點與完成標準。
- 後續 Step 4–11：按需拆解、分工、依賴、核准與迭代狀態。

## 可恢復工作狀態

只為需要分支、中斷或接續的計畫保留以下最小狀態；可放在既有計畫，不強制新建工作板。

- **主線**：穩定的 plan_id、plan_revision、目標／範圍、成功條件、來源位置與已讀版本。主線 step_id 一經引用就不因插入／排序而改號；取消步驟保留 ID 與原因，不再分配。內容、依賴或狀態變更時遞增修訂並記差異。
- **步驟**：step_id、Owner、狀態、依賴的 step_id、可驗收產出。狀態與成果採用分類分開記。
- **分支**：branch_id、parent_step_id 或 parent_branch_id、觸發原因、要回答的問題、範圍、return_to（確切父節點與回到主線的位置）。巢狀分支逐層保存，不能把最後討論的子題當成新主線。
- **分支結果**：逐項分類「已採用／已否決／待驗證」，附依據、限制與受影響的 step_id。已採用不自動表示已部署；待驗證不解除硬依賴；被否決與未試不可混用。
- **Checkpoint**：checkpoint_id、時間／修訂版、目前主線與分支位置、已驗證 artifact 的位置／版本／證據、未完成與阻塞、未同步或結果不明的外部操作（標的、可用 ID、最後觀察、回查方式）、下一個可執行動作及完成條件。未查證不填成已驗證。

### 分支回收與修訂

1. 比對分支結果與原問題，列出採用、否決、待驗證的項目及理由。
2. 沿 return_to 回到父節點；巢狀分支先回上層，不跳失父層剩餘工作。
3. 只更新受影響的主線步驟、硬／軟／外部依賴、驗收與風險；保留其他未完成步驟及原 ID。
4. 如果結果改變已確認目標、範圍或重要取捨，先交使用者裁定，再修訂基線；既有授權內的實作細節不重複核准。未裁定只暫停依賴該決定的段落。
5. 記錄 plan_revision 的變更摘要、checkpoint 與下一個具體動作。恢復時先讀現行計畫與即將操作的來源／外部狀態，對照 checkpoint；舊對話只供背景，不覆寫新版。衝突無法判定時暫停受影響段落。

例如主線 A、B、C、D、E，在 B 開 B1，再細分 B1-a／B1-b／B1-c；這些是 B 的子樹，不能用它們取代 C、D、E。B1 收斂回 B，核對 B 的驗收後才接 C；若 C 的輸入因此改變，只修訂 C 與相依工作。

### 完成與部分成功

依授權範圍定義目的地：來源 artifact、帳號保存內容及適用的 Notion 工作狀態各自有完成證據與回讀；不要求未授權目的地。來源成功但帳號失敗時，主線仍保留帳號同步待辦，不把任務標成全部 Done。來源／帳號保存與實際 Runtime 使用分開；靜態檢查或合成演練不能證明跨 AI／跨對話正式執行成功。

外部操作逾時或結果不明，先查既有標的／ID／版本；確認不存在或缺少哪些部分後才重試缺少部分。無法判定就記「結果未確認」並停止可能重複的寫入。只要求規劃時，上述是計畫的驗收要求，不是執行授權。


# 重要定義

## Phase｜階段

一組共同產生明確成果的任務。

建立階段時，依複雜度選用以下資訊；成果與完成條件保留，核准欄位只有確實需要時才加入：

* 目的
* 主要成果
* 進入條件
* 核心任務
* Checkpoint
* Approval Gate
* Definition of Done

Phase 不應只用工具或部門命名。

較好的名稱：

* 核心架構凍結
* Pilot 建置
* 正式主稿整合
* 驗證與修正

較差的名稱：

* ChatGPT 階段
* Claude 階段
* 資訊室階段

工具與部門是執行者，不是階段成果。

---

## Task｜任務

一個可以由單一 Owner 推動，並產生可驗證輸出的工作單位。

任務欄位候選如下；Light 可合併目的、Input／Action／Output，保留 Owner、實際依賴與可驗證成果：

* 任務名稱
* 目的
* Owner
* Input
* Action
* Output
* Dependency
* 完成標準

任務應使用動詞開頭，例如：

* 確認核心問題
* 彙整三院基線資料
* 更新正式主稿
* 檢查 KPI 與預算一致性

避免：

* 核心問題
* 資料
* Claude
* 預算處理

---

## Owner

對任務完成負主要責任的人。

可另外列：

* Contributors：協作者
* Reviewer：品質檢查者
* Approver：具有正式核准權者
* AI Support：提供協助的 AI

不得用「團隊」作為唯一 Owner，除非團隊內已有明確負責人。

---

## Dependency｜依賴

任務開始或完成所需的前置條件。

分為：

### Hard Dependency

未完成就不能開始。

例如：

* 申請主體未確認，無法完成正式送件架構。
* 原始資料未取得，無法設定正式基線。

### Soft Dependency

可以先暫定前進，但後續需要補正。

例如：

* 可先用暫定名稱撰寫，正式送件前再確認。

### External Dependency

取決於團隊外部的人、單位、系統或政策。

例如：

* 主計室確認。
* 合作單位提供意向書。
* 外部系統權限開通。

每個 Dependency 應說明：

* 由誰解除
* 預期產生什麼
* 未解除時如何處理

---

## Checkpoint｜檢查點

用於確認工作是否朝正確方向前進。

Checkpoint 可以發現問題並要求修正，但原則上不一定阻止後續工作。

例如：

* 初稿可讀性 Review
* Pilot 操作測試
* 資料完整性檢查
* 跨章節一致性檢查

Checkpoint 必須定義：

* 檢查什麼
* 誰檢查
* 通過標準
* 未通過如何處理

---

## Approval Gate｜核准點

必須由具有權限的人明確核准，才能進入下一階段。

例如：

* 總主持人核定核心工作包
* 主計室確認預算科目
* 院方核准正式送件版
* 資安單位核准資料使用方式

Approval Gate 必須定義：

* 核准事項
* Approver
* 核准所需資料
* 可接受結果
* 未核准時回到哪一步

不要把一般 Review 全部升級成 Approval Gate。

---

## Definition of Done｜完成標準

完成標準必須是可觀察、可驗證的狀態。

不接受：

* 已討論
* 已處理
* 大致完成
* 持續追蹤
* 已請相關單位協助

較好的完成標準：

* 總主持人已明確裁定三至五個核心工作包。
* KPI 定義、基線、資料來源及 Owner 均已填寫。
* Claude 已更新正式主稿並回報修改位置。
* 主計室已確認科目可編列。
* Pilot 已完成一次從 Trigger 到 Canonical 更新的完整循環。

---

## Step 4｜拆解任務

每個 Phase 拆成最少必要任務。

需要詳細任務契約時，選用以下欄位：

### Task ID

例如：

* P1-T1
* P1-T2
* P2-T1

### 任務名稱

以動詞開頭。

### 目的

此任務解決什麼問題。

### Owner

唯一主要負責人。

### Contributors

必要協作者。

### AI Support

ChatGPT、Claude、Cowork、Codex 或其他工具的協助角色。

### Input

任務開始前需要什麼。

### Action

實際要做什麼。

### Output

必須產生什麼成果。

### Dependency

Hard、Soft 或 External。

### Checkpoint

如何檢查。

### Approval Gate

是否需要核准。

### Definition of Done

完成的可驗證條件。

不要為只有幾分鐘的微小操作建立獨立 Task，除非它是重要控制點。

---

## Step 5｜指定 Owner 與責任

檢查：

* 每個 Task 是否只有一個 Owner
* 是否把「團隊」當成模糊 Owner
* AI 是否被錯誤指定為最終責任人
* Reviewer 與 Approver 是否混淆
* Decision Owner 是否承擔過多日常工作

若 Owner 尚未確定，標示：

> TBD—需由〔Decision Owner〕在該任務實際開始前指派。

不要自行補造姓名。

---

## Step 6｜建立依賴關係

針對每個 Task 判斷：

* 可以立即開始
* 必須等待前一任務
* 可以平行進行
* 依賴外部單位
* 可用工作假設先前進

特別找出：

### Critical Dependency

一旦延誤，就會阻塞多項後續工作的依賴。

### Single Point of Failure

只有一個人、資料或系統能完成，失效後沒有替代方案。

### Hidden Dependency

原 Implementation Plan 未明確寫出，但實際執行必須具備的條件。

本 Skill只指出依賴，不執行完整風險紅隊。

---

## Step 7｜設定 Checkpoint

Checkpoint 應放在：

* 高成本工作開始前
* 不可逆修改前
* 跨 AI 或跨工具交班後
* Pilot 完成後
* 正式內容進入 Canonical 前
* 大量複製或全面部署前

每個 Checkpoint 說明：

* 檢查內容
* Reviewer
* 輸入
* 通過條件
* 未通過的修正路徑

不要每天都設立形式化 Checkpoint。

---

## Step 8｜設定 Approval Gate

下列事項可能需要正式核准；先確認既有授權與實際權責要求，並非每次出現就新增核准：

* 核心策略
* 架構變更
* 預算
* 法規或資安
* 正式版本
* 不可逆操作
* 對外發布
* 全面部署

每個 Approval Gate 說明：

* Gate 名稱
* Approver
* 待核准內容
* 所需證據
* 核准結果
* 未核准時的回退位置

若只是一般品質檢查，使用 Checkpoint，不要升級為 Approval Gate。

---

## Step 9｜定義完成標準

依計畫實際存在的層級定義；Light 不需新增 Phase。

### Task Definition of Done

單一任務完成的驗證條件。

### Phase Definition of Done

該階段所有必要成果與核准是否完成。

### Overall Definition of Done

依本次範圍選用整體完成條件；只交付文件不要求上線，無長期系統不要求 Canonical 或維護交接：

* 功能或流程可運作
* 正式產出存在
* Canonical 已正確更新
* 必要核准完成
* Owner 接手維護
* 驗證通過
* 回復方式已確認
* 尚待處理事項已明確交班

---

## Step 10｜建立迭代循環

每個 Phase 結束後執行：

1. 檢查實際完成成果。
2. 比較原計畫與實際差異。
3. 確認假設是否成立。
4. 關閉或更新 Dependency。
5. 決定下一階段：

   * 照原計畫前進
   * 修正後前進
   * 暫停
   * 回到前一階段
   * 回到 Implementation Bridge
6. 只重新細化下一個 Phase，不必重寫全部計畫。

---

## Step 11｜建立狀態規則

需要工作板且尚無既有狀態規則時，可從以下狀態選用：

* Not Started
* Ready
* In Progress
* Blocked
* Review
* Awaiting Approval
* Done
* Dropped

狀態定義：

### Not Started

尚未開始，且前置條件未必完成。

### Ready

前置條件已完成，可立即開始。

### In Progress

Owner 正在執行。

### Blocked

因依賴、決策或資源無法前進。

### Review

成果已產生，等待 Checkpoint。

### Awaiting Approval

等待正式 Approval Gate。

### Done

已符合 Definition of Done。

### Dropped

經 Decision Owner 決定不再執行。

不要建立過多自訂狀態。

---
