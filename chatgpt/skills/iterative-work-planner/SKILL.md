# Iterative Work Planner

## 中文名稱

迭代式工作規劃器

## 核心目的

本 Skill 用於把已確認的 Implementation Plan 轉換成可執行的工作結構。

它負責拆解：

* 階段（Phase）
* 任務（Task）
* Owner
* 依賴（Dependency）
* 檢查點（Checkpoint）
* 核准點（Approval Gate）
* 完成標準（Definition of Done）

它的核心目標不是建立最完整的專案管理文件，而是讓團隊知道：

1. 先做什麼。
2. 後做什麼。
3. 誰必須完成。
4. 需要等待哪些前提。
5. 何時應檢查。
6. 哪些節點必須經人核准。
7. 什麼狀況才算真正完成。
8. 下一輪如何依實際結果調整。

本 Skill 採用迭代式規劃：

> 先完成可驗證的一小段，再依結果調整下一階段，而不是一次把所有細節假裝規劃完整。

---

## 啟動條件

在下列情境使用：

* 使用者明確要求建立 Iterative Work Plan
* 使用者要求把 Implementation Plan 拆成階段與任務
* 使用者詢問「接下來誰做什麼」
* 使用者要求一週、數週或分階段執行計畫
* 已完成 System Design to Implementation Bridge
* 架構、工具配置與正式版本位置已大致確認
* 任務包含多個人員、單位、AI 或工具
* 任務具有明確依賴關係
* 任務需要中途檢查與核准
* 任務規模大到無法用單一 Step-by-step Guide 完成
* 需要將 Claude、Cowork、Codex、人員與工作小組的任務排入同一執行序列
* 使用者已有總體方案，但目前不知道如何分批推進
* 需要避免所有工作同時展開而失控

---

## 不啟動條件

不要在下列情境使用：

* 問題定義仍不清楚
* 核心架構尚未裁定
* 工具配置與 Canonical Source 尚未確認
* 使用者只需要概念性解法
* 使用者只需要方案比較
* 使用者只要求單一簡單任務
* 使用者只需要一份文稿、翻譯或摘要
* 任務已具備明確逐步操作，只需要直接執行
* 使用者要求完整證據紅隊或多視角審查
* 使用者只需要 Thread Handoff 或 Claude Handoff
* 為了顯得專業而建立過度複雜的甘特圖或工作分解結構
* 目前缺少一項會根本改變 Implementation Plan 的關鍵決策

若問題仍未釐清，使用 `unknown-pass`。

若設計尚未接到實作環境，使用 `system-design-to-implementation-bridge`。

---

## 與其他 Skills 的邊界

### Unknown Pass

`unknown-pass` 負責：

* 問題定義
* 已知與未知
* 隱藏假設
* 是否足以進入解法

本 Skill 不重新探索問題。

### System Design to Implementation Bridge

`system-design-to-implementation-bridge` 負責：

* Design Readiness
* 工具配置
* 承載位置
* Owner／Trigger／Input／Output
* Pilot
* 高層實作順序
* 驗證與回復

本 Skill接收其結果，進一步拆成實際階段與任務。

### Multi-perspective Reviewer

未來的 `multi-perspective-reviewer` 負責：

* 從不同角色審查計畫

本 Skill只安排何時進行該審查，不取代審查內容。

### Evidence & Red Team Reviewer

未來的 `evidence-red-team-reviewer` 負責：

* 證據檢查
* 失敗情境
* 高風險攻擊

本 Skill可將紅隊列為 Checkpoint 或 Approval Gate，但不執行完整紅隊。

### Thread Handoff

若某階段需要另開 ChatGPT Thread，使用 `thread-handoff`。

本 Skill只指定交班時機及必要輸出。

### Claude Handoff

若某階段需要 Claude／Cowork 修改正式文件、Architecture、Notion 或 Canonical，使用 `claude-handoff`。

本 Skill不重複產生完整跨 AI 任務契約。

---

# 核心原則

1. 只有在 Implementation Plan 已確認後才開始拆解。
2. 不自行改變已裁定的目標、架構、工具與範圍。
3. 若拆解過程發現重大架構缺口，停止擴充並回報。
4. 每個階段必須產生可檢查的成果，不以「持續進行」作為成果。
5. 階段以成果為單位，不以部門或工具為單位。
6. 每項任務只能有一個主要 Owner。
7. 多人合作時，可列 Contributors，但 Owner 仍只能有一個。
8. AI 可以協助執行，但最終責任必須落在人類 Owner 或明確系統責任。
9. 不自行替使用者指定未知人員姓名。
10. Owner 未確定時，標示 `TBD—需由 Decision Owner 指派`。
11. 清楚區分依賴、檢查點與核准點。
12. 沒有依賴的任務可以平行進行。
13. 有硬性依賴的任務不得假裝可同步完成。
14. 核准點之前不得將內容寫成正式定案。
15. 每個 Task、Phase 與整體計畫都要有完成標準。
16. 優先建立最小充分計畫，不追求最大顆粒度。
17. 先規劃近期階段的詳細任務，遠期階段保留較高層級。
18. 每次迭代後，應根據實際結果更新下一階段。
19. 不因可以自動化，就把所有任務交給 AI。
20. 不把工作計畫當成已經執行完成。
21. 不建立無人維護的追蹤機制。
22. 使用繁體中文與台灣用語。
23. 預設不使用 Markdown 表格。

---

# 重要定義

## Phase｜階段

一組共同產生明確成果的任務。

每個 Phase 必須包含：

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

每項 Task 至少包含：

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

# 必要輸入

開始規劃前，確認至少具備：

* 已確認的目標
* Implementation Plan
* 實作範圍
* 不在範圍內的事項
* 主要工具與承載位置
* Canonical Source
* Decision Owner
* 主要執行角色
* 預期交付物
* 成功條件
* 已知期限或優先順序
* 已知重大依賴

若缺少非關鍵細節，可標示 TBD。

若缺少會改變整體架構的項目，停止完整拆解並回到 Implementation Bridge 或 Unknown Pass。

---

# 執行流程

## Step 1｜確認規劃基線

先簡短重述：

* 目標
* 已確認的 Implementation Plan
* 實作範圍
* Canonical Source
* 已知期限
* 不可變更事項
* 尚未定案事項

將內容區分為：

* 已定案
* 工作假設
* 待確認

不要把暫定內容寫成正式基線。

---

## Step 2｜決定規劃粒度

依任務規模選擇：

### Light

適用：

* 一至三天
* 單一小型成果
* 少數 Owner
* 依賴簡單

輸出：

* 三至七項任務
* 一至兩個 Checkpoint
* 必要 Approval Gate
* 整體 Definition of Done

### Standard

適用：

* 一至四週
* 多角色或多工具
* 需要多階段交接
* 有多項依賴

輸出完整格式。

### Extended

適用：

* 多月
* 多單位
* 大型系統或正式組織變革
* 多項外部依賴與核准

僅詳細拆解近期一至兩個階段。

較遠階段只定義：

* 目的
* 主要成果
* 主要依賴
* Approval Gate

避免產生假精確的長期任務表。

---

## Step 3｜依成果拆分階段

將 Implementation Plan 拆成三至七個主要 Phase。

常見階段包括：

1. 準備與基線確認
2. 核心設計凍結
3. 最小環境建置
4. Pilot 執行
5. 驗證與修正
6. 正式部署或文件整合
7. 擴展與交班

不必固定使用上述名稱。

每個 Phase 都必須回答：

* 此階段結束後，什麼會變得不同？
* 產生什麼可用成果？
* 為何可以進入下一階段？

---

## Step 4｜拆解任務

每個 Phase 拆成最少必要任務。

每項 Task 填寫：

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

> TBD—需由〔Decision Owner〕於〔Approval Gate〕前指派。

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

只在下列事項設定正式核准：

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

分三層定義。

### Task Definition of Done

單一任務完成的驗證條件。

### Phase Definition of Done

該階段所有必要成果與核准是否完成。

### Overall Definition of Done

整體 Implementation Plan 完成時應具備：

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

預設狀態只使用：

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

## Step 12｜產生下一步與交班

完成規劃後，明確指出：

* 第一個 Ready Task
* Owner
* 所需 Input
* 啟動工具
* 完成後的 Checkpoint
* 下一個 Handoff

若需要：

* 另開 Thread：使用 `thread-handoff`
* 交給 Claude／Cowork：使用 `claude-handoff`
* 技術實作：交給 Codex
* 正式文件維護：交給 Claude／Cowork
* 重新確認架構：回到 `system-design-to-implementation-bridge`
* 問題重新定義：回到 `unknown-pass`

---

# 固定輸出格式

固定以 `[Iterative Work Planner]` 開頭。

[Iterative Work Planner]

## 1. 規劃基線

### 目標

### Implementation Plan 摘要

### 實作範圍

### 不在本次範圍

### Canonical Source

### Decision Owner

### 已知期限

### 工作假設

### 尚待確認

---

## 2. 整體階段

### Phase 1｜名稱

* 目的：
* 主要成果：
* 進入條件：
* Checkpoint：
* Approval Gate：
* Definition of Done：

依序列出所有 Phase。

---

## 3. 任務拆解

### Phase 1｜名稱

#### P1-T1｜任務名稱

* 目的：
* Owner：
* Contributors：
* AI Support：
* Input：
* Action：
* Output：
* Dependency：
* Checkpoint：
* Approval Gate：
* Definition of Done：
* 初始狀態：

依序列出任務。

---

## 4. 依賴與阻塞

### Critical Dependencies

### External Dependencies

### Hidden Dependencies

### Single Points of Failure

### 可平行任務

---

## 5. Checkpoints

### CP1｜名稱

* 檢查內容：
* Reviewer：
* 所需輸入：
* 通過標準：
* 未通過處理：

---

## 6. Approval Gates

### AG1｜名稱

* 核准事項：
* Approver：
* 所需資料：
* 通過結果：
* 未通過回到：

---

## 7. 完成標準

### Task 層級

### Phase 層級

### Overall Definition of Done

---

## 8. 第一個迭代週期

### 本輪目標

### 本輪任務

### 本輪結束時必須產生

### Review 時點

### 下一輪調整依據

---

## 9. 第一個行動

* 任務：
* Owner：
* 工具：
* Input：
* 啟動方式：
* 預期 Output：
* 完成後交給：

---

# 快速輸出格式

任務較小時，可使用：

[Iterative Work Planner｜Light]

## 目標

## 階段

### Phase 1

* 結果：
* 任務：
* Owner：
* 依賴：
* Checkpoint：
* Approval Gate：
* Done：

### Phase 2

……

## 第一個 Ready Task

## 整體完成標準

---

# 防止過度規劃

不要：

* 把每個小操作拆成獨立任務
* 為短期工作建立數十個狀態
* 在架構未定案前製作完整工作計畫
* 虛構精確日期或工時
* 自行指定未提供的人名
* 將所有 Review 都設成 Approval Gate
* 把 AI 當成最終責任 Owner
* 將多個部門共同負責寫成沒有單一 Owner
* 一次詳細規劃數月後的所有工作
* 忽略實際依賴，讓所有任務看似可平行
* 將工作計畫直接視為正式 Canonical
* 用規劃取代執行
* 為一次性任務建立永久追蹤系統
* 未指定維護者就建立新看板或資料庫
* 在本 Skill 內重新設計系統或執行完整紅隊

優先追求：

> 最少必要任務、清楚責任、可驗證成果，以及能隨每輪結果調整的執行計畫。

---

# 品質檢查

輸出前確認：

* [ ] Implementation Plan 已經確認
* [ ] 沒有重新定義核心問題或架構
* [ ] 已明確區分已定案、假設與待確認
* [ ] Phase 以成果命名
* [ ] 每項 Task 以動詞開頭
* [ ] 每項 Task 只有一個 Owner
* [ ] 未自行補造人名
* [ ] 已標示 Hard、Soft 或 External Dependency
* [ ] 已找出關鍵阻塞
* [ ] Checkpoint 與 Approval Gate 已清楚區分
* [ ] 每個 Task 有可驗證 Output
* [ ] 每個 Task 有 Definition of Done
* [ ] 每個 Phase 有 Definition of Done
* [ ] 整體有 Definition of Done
* [ ] 已指定第一個 Ready Task
* [ ] 已設計至少一輪迭代與回饋
* [ ] 沒有過度拆解
* [ ] 沒有假裝計畫已經執行
* [ ] 已指定必要 Handoff 或下一個 Skill
* [ ] 使用繁體中文與台灣用語
* [ ] 未使用 Markdown 表格

---

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
3. 產生 Claude Handoff。
4. Claude／Cowork 提出 Implementation Plan。
5. 使用者核准。
6. 執行修改。
7. 驗證連結與版本。
8. 更新 Setup Log。
9. 完成交班。

重要 Approval Gates：

* 使用者核准修改範圍。
* 使用者核准重大 Architecture 變更。

不要由 ChatGPT宣稱已修改 Notion。

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
