# System Design to Implementation Bridge

## 中文名稱

系統設計到實作橋接

## 核心目的

本 Skill 用於處理以下缺口：

> 概念與架構已經討論完成，但仍不知道如何放進現有工具、工作流與日常操作中。

本 Skill 不重新設計整個系統，而是將已收斂的設計轉換成：

* 實際承載位置
* 工具分工
* 人員與 AI 責任
* 啟動條件
* 輸入與輸出
* 操作順序
* Step-by-step Guide
* 驗證方式
* 回復與停止方式

最終目標是讓使用者能回答：

1. 接下來在哪個工具操作？
2. 建立或修改什麼？
3. 由誰負責？
4. 什麼時候啟動？
5. 要提供什麼輸入？
6. 預期產生什麼輸出？
7. 如何交給下一個人或 AI？
8. 如何確認系統真的能運作？
9. 發生問題時如何回復？

---

## 啟動條件

在下列情境使用：

* 使用者明確要求「幫我實作這個系統」
* 使用者詢問「下一步怎麼做」
* 使用者詢問「應該放在哪個工具」
* 使用者詢問「如何使用目前的 AI 工作流完成」
* 使用者要求 Step-by-step Guide
* 概念性解法或 Architecture 已大致收斂
* 已經提出流程、角色或工具，但尚未說明如何操作
* 討論中提出新 Thread、Project、Skill、Database、看板、Agent、文件或自動化
* 需要將 ChatGPT 討論交給 Claude、Cowork 或 Codex 實際落地
* 需要決定 Canonical Source 與版本管理位置
* 需要將新流程嵌入既有日常工作
* 使用者指出「這個建議很好，但實際上怎麼做？」

---

## 不啟動條件

不要在下列情境使用：

* 問題定義仍高度模糊
* 核心目標與成功條件尚未釐清
* 使用者只是要求腦力激盪或方案比較
* 使用者只要求改寫、翻譯、摘要或一般文稿
* 使用者只要求完整紅隊審查
* 使用者只要求研究或搜尋證據
* 使用者只要求拆解大型專案任務
* 使用者已經提供明確操作步驟，只需要直接執行
* 任務純粹是程式撰寫，且已可直接交給 Codex
* 使用者只需要 Thread Handoff 或 Claude Handoff
* 為了顯得完整而無必要地設計新系統

若核心問題仍未釐清，建議先使用 `unknown-pass`，不要在本 Skill 內重新執行完整 Unknown Pass。

---

## 與其他 Skills 的邊界

### Unknown Pass

`unknown-pass` 負責：

* 問題定義
* 已知與未知
* 隱藏假設
* 是否足以進入解法階段

本 Skill 只做最低限度的重要未知檢查，不重新展開完整探索。

### Iterative Work Planner

未來的 `iterative-work-planner` 負責：

* 階段拆解
* 詳細任務
* 時程
* 依賴
* 檢查點
* 核准點
* 進度追蹤

本 Skill 只提供足以啟動的實作順序，不建立完整專案計畫。

### Multi-perspective Reviewer

未來的 `multi-perspective-reviewer` 負責多角色審查。

本 Skill 只確認必要角色是否有 Owner、Reviewer 或 Approver，不執行完整多視角分析。

### Evidence & Red Team Reviewer

未來的 `evidence-red-team-reviewer` 負責證據與失敗風險審查。

本 Skill 只標示需要驗證的重大假設，不執行完整紅隊。

### Thread Handoff

若需要讓新的 ChatGPT Thread 接手，使用 `thread-handoff`。

本 Skill 可以指出需要建立新 Thread，但不取代正式 Thread Handoff。

### Claude Handoff

若需要 Claude／Cowork 修改正式文件、Notion、Architecture、INDEX、Registry 或 Canonical，使用 `claude-handoff`。

本 Skill決定「應該交給誰及交付什麼」，但不重複產生完整 Claude Handoff。

---

## 核心原則

1. 先確認設計是否已足以實作。
2. 優先使用使用者現有工具，不因概念新穎就增加新工具。
3. 工具不是解法，工具只承載已確定的操作模式。
4. 不把「建立文件、看板或資料庫」本身當成實作完成。
5. 每個新產物都必須有 Owner、Trigger、Input、Output 與維護方式。
6. 每項正式內容只能有一個 Canonical Source。
7. ChatGPT 討論稿、Claude 正式稿與 Notion Canonical 必須區分。
8. 不假設不同 Thread、Project 或 AI 自動共享全部脈絡。
9. 交接必須透過明確摘要、Handoff 或正式參考資料。
10. 先完成最小可行試運轉，再擴充完整系統。
11. 第一個 Pilot 應小到可以完成一個完整循環。
12. 實作方案必須包含驗證與回復方式。
13. 若實作需要持續維護，必須指定維護人與更新頻率。
14. 若無人維護，優先採用更簡單的操作方式。
15. 不因可以自動化就立即自動化。
16. 先證明人工或半人工流程可運作，再評估自動化。
17. 不自行修改正式 Architecture、Notion 或 Canonical。
18. 不宣稱尚未執行的步驟已完成。
19. 使用繁體中文與台灣用語。
20. 預設不用 Markdown 表格。

---

# 執行流程

## Step 1｜重述已完成的設計

先用簡短內容說明：

* 要解決的問題
* 已採用的概念性解法
* 已確認的核心架構
* 使用者期待的實作結果

必須標示：

* 已定案
* 暫定採用
* 尚待確認

不要在此重新展開完整設計討論。

---

## Step 2｜Design Readiness Check

只做最低限度的設計成熟度檢查。

檢查以下項目：

### 目標

* 要解決的問題是否清楚？
* 使用者期待的結果是否清楚？
* 是否知道何時算成功？

### 範圍

* 實作範圍是否清楚？
* 哪些內容不在本次範圍？
* 是否有持續擴張的風險？

### 角色

* Decision Owner 是否明確？
* 執行 Owner 是否明確？
* Reviewer／Approver 是否明確？

### 操作模式

* 流程如何啟動？
* 主要輸入與輸出是否可描述？
* 正式版本放在哪裡？
* 不同工具如何交班？

### 可行性

* 所需工具是否存在？
* 人員是否有權限與能力使用？
* 是否需要持續維護？
* 是否有明顯的法規、安全或資料限制？

Design Readiness 只能給出三種判斷：

### Ready

核心設計足以進入實作。

### Ready with Assumptions

可在明確工作假設下進入小規模試運轉。

必須列出：

* 採用的假設
* 可能影響
* 第一個驗證點

### Not Ready

仍有一項會實質改變架構的關鍵問題。

此時：

* 不產生完整實作系統
* 只指出最重要的缺口
* 建議使用 `unknown-pass`
* 一次只提出一個最重要問題

---

## Step 3｜最低限度的重要未知檢查

只檢查會影響實作的未知，不重新執行完整 Unknown Pass。

優先檢查：

* 正式版本由誰維護？
* 使用者是否真的擁有所需工具與權限？
* 不同 AI 或 Thread 是否能直接存取彼此內容？
* 誰會持續更新？
* 是否有不可逆修改？
* 是否涉及敏感資料、資安、法規或權限？
* 若核心人員未執行，流程是否仍能運作？
* 是否需要新的工具，還是現有工具已足夠？
* 是否存在兩個 Canonical Source？
* 是否將討論稿誤當正式內容？

將未知分為：

* 實作前必須確認
* 可用工作假設前進
* 可在 Pilot 後補充

不要列出與當前實作無關的未知。

---

## Step 4｜選擇實作模式

依需求選擇最簡單可行模式。

### Mode A｜單一 Chat 實作

適合：

* 短期
* 單一交付物
* 不需跨 AI
* 不需長期維護

### Mode B｜ChatGPT Project＋多 Thread

適合：

* 同一專案有不同工作流
* 需要分開討論與正式工作
* 需要 Project Instruction 與共同參考資料
* 不同 Thread 需透過 Handoff 交接

### Mode C｜ChatGPT＋Claude

適合：

* ChatGPT 負責探索、收斂與紅隊
* Claude 負責長文件整合、正式版本與一致性
* 使用者負責裁定

### Mode D｜Claude Cowork 執行

適合：

* 架構已明確
* 需要多步驟檔案或知識工作
* 需要更新正式文件、Architecture、INDEX 或 Registry

### Mode E｜Codex 技術實作

適合：

* 程式
* 自動化
* 資料處理
* 批次修改
* 測試
* GitHub

### Mode F｜Notion Canonical

適合：

* 已定案知識
* 正式架構
* 決策紀錄
* 長期維護
* 狀態與版本管理

### Mode G｜混合模式

僅在單一工具明顯不足時採用。

必須說明：

* 每個工具的角色
* 交接點
* Canonical Source
* 哪個工具不能做什麼

不要因使用者擁有多種工具，就強迫所有工具都參與。

---

## Step 5｜Tool Mapping

對每個需要使用的工具說明：

### Tool

工具名稱。

### Purpose

它在本流程中解決什麼問題。

### Location

實際放在哪個 Project、Thread、資料夾、文件或頁面。

### Owner

誰負責操作與維護。

### Trigger

什麼情況會啟動。

### Input

需要提供什麼。

### Output

必須產生什麼。

### Handoff

下一步交給誰、使用哪一種 Handoff。

### Canonical Status

該工具中的內容是：

* 討論稿
* 工作稿
* 暫定稿
* 正式稿
* Canonical

不要只列工具名稱。

---

## Step 6｜建立最小操作契約

每個核心流程至少定義：

### Owner

必須推動完成的人。

### Trigger

啟動條件。

### Input

啟動時需要的資料、決策或文件。

### Action

實際執行的動作。

### Output

完成後產生的可驗證成果。

### Reviewer／Approver

誰檢查或裁定。

### Handoff

交給下一個角色或工具的方式。

### Canonical Source

正式版本的位置。

### Failure Path

無法完成或資訊不足時如何處理。

---

## Step 7｜選擇第一個 Pilot

不要直接全面上線。

第一個 Pilot 應符合：

* 規模小
* 可以完成整個循環
* 結果容易驗證
* 不涉及高風險不可逆修改
* 可以測試主要交接點
* 失敗成本低

Pilot 必須測試：

1. Trigger 是否清楚。
2. Input 是否足夠。
3. Owner 是否真的會執行。
4. 工具交接是否可行。
5. Output 是否可使用。
6. Canonical 是否正確更新。
7. 是否增加不必要維護負擔。

若無法指定 Pilot，代表實作設計可能仍過大或過於抽象。

---

## Step 8｜建立實作順序

只提供足以啟動與試運轉的順序，不取代完整 Iterative Work Planner。

建議使用以下階段：

### Phase 0｜準備

* 確認已定案設計
* 確認工具與權限
* 確認 Owner
* 確認 Canonical Source

### Phase 1｜建立最小承載環境

* 建立必要 Thread、Project、文件或資料夾
* 不建立非必要資料庫或自動化
* 放入必要 Instruction 與參考資料

### Phase 2｜執行 Pilot

* 使用一個真實案例
* 完成完整操作循環
* 記錄問題

### Phase 3｜驗證與修正

* 檢查結果
* 修正交接、責任或工具配置
* 確認維護負擔

### Phase 4｜擴展

* Pilot 成功後才複製到其他模組、團隊或文件
* 必要時交給 Iterative Work Planner 做完整拆解

---

## Step 9｜產生 Step-by-step Guide

逐步指南必須具體到使用者可以操作。

每一步至少包含：

### Step 編號與名稱

### 使用工具

在哪一個工具中操作。

### 操作位置

Project、Thread、文件、頁面或資料夾。

### 執行者

誰操作。

### 操作內容

實際建立、貼入、修改、確認或送出的內容。

### 輸入

需要準備的資料。

### 預期結果

完成後應看到什麼。

### 驗證

如何確認這一步正確。

### 下一步

交給誰或進入哪個工具。

不要使用以下空泛表述：

* 建立一個頁面
* 開一個 Thread
* 交給 Claude
* 建立看板
* 使用自動化
* 更新 Architecture

除非同時說明具體位置、內容、Owner、輸入、輸出與驗證。

---

## Step 10｜驗證計畫

驗證至少分成四層。

### 操作驗證

流程是否可以從頭走到尾。

### 內容驗證

輸出是否正確、完整、可使用。

### 交接驗證

下一個人或 AI 是否能理解並接續。

### 治理驗證

正式版本、權限、Owner 與決策紀錄是否正確。

可選擇的成功指標包括：

* 不需要主持人重複解釋背景
* 沒有產生兩份正式版本
* Handoff 可被下一個 AI 正確執行
* Owner 知道何時與如何更新
* Pilot 能在預期時間內完成
* 產出可直接進入下一階段
* 未增加無人維護的新文件或系統

---

## Step 11｜回復與停止方式

每個實作方案至少說明：

### 何時停止

例如：

* Pilot 無法完成
* 維護成本高於效益
* Owner 不明
* 工具無法交接
* 產生版本分歧
* 關鍵安全或法規問題未解決

### 如何回復

例如：

* 回到原有人工流程
* 恢復前一版正式文件
* 關閉暫時建立的 Thread 或資料庫
* 停止自動化
* 保留實驗紀錄但不進入 Canonical
* 將未定案內容移回討論區

### 誰有權決定回復

明確指定 Decision Owner。

不要將回復方式寫成「必要時再處理」。

---

## Step 12｜指定下一個工具或 Skill

本 Skill 完成後，只能導向明確下一步。

可能包括：

* 直接開始 Pilot
* 使用 `thread-handoff`
* 使用 `claude-handoff`
* 交給 Codex 執行技術工作
* 交給 Claude Cowork 執行正式修改
* 使用 Iterative Work Planner 做完整拆解
* 回到 `unknown-pass`
* 由使用者先做架構裁定
* 不需要新工具，沿用現有工作流

---

# 固定輸出格式

固定以 `[System Design to Implementation Bridge]` 開頭。

[System Design to Implementation Bridge]

## 1. 已收斂的設計

### 要解決的問題

### 已採用的概念性解法

### 已確認的架構

### 尚未定案

---

## 2. Design Readiness Check

### 判斷

只能選擇：

* Ready
* Ready with Assumptions
* Not Ready

### 理由

### 實作前必須確認

### 可採工作假設

---

## 3. 建議實作模式

### 模式

### 為何選擇

### 不建議的替代方式

說明為何不需要其他工具、文件或系統。

---

## 4. Tool Mapping

逐一列出：

### 工具一

* Purpose：
* Location：
* Owner：
* Trigger：
* Input：
* Output：
* Handoff：
* Canonical Status：

### 工具二

依需要增加。

---

## 5. Operating Contract

### 流程名稱

* Owner：
* Trigger：
* Input：
* Action：
* Output：
* Reviewer／Approver：
* Handoff：
* Canonical Source：
* Failure Path：

依需要增加核心流程。

---

## 6. 第一個 Pilot

### Pilot 範圍

### 為何選擇

### 預期完成循環

### 成功標準

### 停止條件

---

## 7. 實作順序

### Phase 0｜準備

### Phase 1｜建立最小環境

### Phase 2｜執行 Pilot

### Phase 3｜驗證與修正

### Phase 4｜擴展

若任務很小，可合併階段。

---

## 8. Step-by-step Guide

### Step 1｜……

* 工具：
* 位置：
* 執行者：
* 操作：
* 輸入：
* 預期結果：
* 驗證：
* 下一步：

依實際需求繼續。

---

## 9. 驗證方式

### 操作驗證

### 內容驗證

### 交接驗證

### 治理驗證

---

## 10. 回復方式

### 停止條件

### 回復步驟

### Decision Owner

---

## 11. 下一個動作

明確指出：

* 現在由誰
* 在哪個工具
* 完成哪一件事
* 完成後交給誰

若需使用其他 Skill，明確指定 Skill 名稱。

---

# 快速輸出格式

若系統簡單，可使用：

[Implementation Bridge｜Light]

## Readiness

## 實作位置

## Owner／Trigger／Input／Output

## Step-by-step

1. ……
2. ……
3. ……

## 驗證

## 回復

## 下一步

---

# Design Readiness 最低標準

只有下列條件大致成立，才可判定 Ready：

* [ ] 問題與目標清楚
* [ ] 成功條件可描述
* [ ] 實作範圍清楚
* [ ] Decision Owner 明確
* [ ] 執行 Owner 明確
* [ ] 主要輸入與輸出清楚
* [ ] 工具與承載位置可指定
* [ ] Canonical Source 可指定
* [ ] 主要交接點清楚
* [ ] 沒有未處理的重大安全、法規或權限問題
* [ ] 可以選出小規模 Pilot
* [ ] 可以說明如何驗證與回復

不要求所有細節都完整，但不能以想像補足關鍵架構。

---

# 工具配置指引

## ChatGPT Chat

適合：

* 問題討論
* 架構收斂
* 方案比較
* 決策支援
* 紅隊與 Review
* 產生 Handoff

不適合：

* 作為唯一長期 Canonical
* 假設其他 Thread 自動讀取所有內容
* 取代正式版本管理

## ChatGPT Project

適合：

* 集中同一專案的 Thread、檔案與 Instruction
* 維持專案背景
* 分開不同工作流

需要注意：

* 跨 Thread 資訊仍應正式交班
* 不將所有聊天都當成正式知識

## ChatGPT Work

若可使用，適合：

* 已定義清楚的多步驟知識工作
* 產生完整交付物
* 執行有明確輸入、輸出與驗證的任務

不適合：

* 取代未完成的策略與架構討論

## Codex

適合：

* 程式
* 自動化
* 批次處理
* 測試
* GitHub
* 技術實作

啟動前必須具備：

* 明確需求
* 輸入與輸出
* 影響範圍
* 測試與回復方式

## Claude Chat

適合：

* 長文件整合
* 正式內容整理
* 名詞與版本一致性
* Canonical 草稿維護

需要注意：

* 只接收已定案或清楚標示暫定的內容
* 不自行改變策略

## Claude Cowork

適合：

* 按 Implementation Plan 修改正式文件
* 管理多步驟落地工作
* 維護 Architecture、INDEX、Registry、Canonical

需要注意：

* 修改範圍必須明確
* 必須回報變更、驗證與偏離

## Notion

適合：

* 已定案知識
* 決策紀錄
* Canonical
* 長期狀態與正式架構

不適合：

* 自動保存所有聊天
* 儲存大量未定案腦暴
* 在操作機制未確定前建立複雜資料庫

---

# 使用範例一｜Proposal Operating System

使用者：

「POS 已經討論得差不多，現在要怎麼實作？」

正確行為：

1. 確認已定案內容：

   * POS／Command Thread
   * 計畫書一 Thread
   * 計畫書二 Thread
   * ChatGPT 負責探索與紅隊
   * Claude 負責正式整合
   * 主持人負責裁定

2. 進行 Design Readiness Check。

3. 建議使用：

   * ChatGPT Project 承載三個 Thread
   * Claude 維護正式主稿
   * Notion 只保存已定案 POS 與 Canonical
   * 不先建立一週作戰板或複雜資料庫

4. 選擇第一個 Pilot：

   * 計畫書一的核心問題與三節點定位

5. 提供逐步操作：

   * 建立 Proposal 1 Thread
   * 貼入 Thread Handoff
   * 與 ChatGPT 討論
   * 主持人標示已定案
   * 使用 Claude Handoff
   * Claude 更新正式主稿
   * Claude 回報差異
   * ChatGPT Review

6. 定義成功：

   * 不需重複解釋背景
   * 正式稿只有一份
   * Claude 可正確更新
   * 主持人可以直接核定修改

不要直接把「建立一週作戰板」當作 POS 實作完成。

---

# 使用範例二｜AI 人生故事照護流程

使用者：

「人生故事照護模式已討論完成，怎麼放到目前工作流？」

正確行為：

* 確認誰收集故事、誰確認內容、誰使用、資料放哪裡
* 確認是否涉及敏感個資
* 建議先用少數個案 Pilot
* 指定 ChatGPT 協助訪談稿與摘要
* 指定正式紀錄位置
* 指定照護團隊 Review
* 設定病人或代理人同意
* 定義如何驗證故事是否真的進入照護計畫
* 說明如何停止與刪除資料

不要直接建立完整 AI 平台或新資料庫。

---

# 使用範例三｜建立自動化

使用者：

「這個人工流程已經測過，想改成自動化。」

正確行為：

* 確認人工流程已穩定
* 說明哪些步驟可自動化
* 保留人類核准點
* 定義輸入、輸出、錯誤處理與回復
* 指定由 Codex 或 Cowork 執行
* 必要時使用 Claude Handoff
* 先建立測試環境
* 驗證後才正式啟用

不要因為技術可行，就直接全面自動化。

---

# 防止過度工程化

不要：

* 同時建立多個新 Thread、Database、Skill 與 Agent
* 將一次性任務設計成永久系統
* 為每個流程建立獨立 Canonical
* 因為工具可用就全部納入
* 在沒有 Owner 時建立需持續維護的產物
* 把流程圖當成實作完成
* 把 Implementation Plan 當成已執行
* 未測試就全面上線
* 未指定回復方式就修改正式系統
* 在本 Skill 內重新執行完整 Unknown Pass、工作拆解或紅隊

優先選擇：

> 最少工具、最少交接、最少維護，但足以完成目標的實作方式。

---

# 品質檢查

輸出前確認：

* [ ] 設計已大致收斂
* [ ] 已完成 Design Readiness 判斷
* [ ] 沒有重新執行完整 Unknown Pass
* [ ] 只列與實作有關的重要未知
* [ ] 沒有把工具本身當成解法
* [ ] 優先使用現有工具
* [ ] 每個工具都有 Purpose 與 Location
* [ ] 核心流程有 Owner、Trigger、Input、Output
* [ ] Canonical Source 明確
* [ ] 已指定第一個 Pilot
* [ ] 實作順序足以啟動，但未取代完整工作規劃
* [ ] Step-by-step Guide 具體可操作
* [ ] 已說明驗證方式
* [ ] 已說明停止與回復方式
* [ ] 已指出下一個工具或 Skill
* [ ] 未取代 Thread Handoff 或 Claude Handoff
* [ ] 未宣稱尚未執行的修改已完成
* [ ] 使用繁體中文與台灣用語
* [ ] 未使用 Markdown 表格
