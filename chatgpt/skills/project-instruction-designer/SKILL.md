---
name: project-instruction-designer
description: "[TODO: 請填入 project-instruction-designer 的用途與使用時機；此為待填 placeholder。]"
---

# Project Instruction Designer

**中文名稱：Project Instruction 設計與修訂**  
**版本：v1.1｜2026-09-06**

## 核心目的

將 Project Instruction 設計成特定 Project 內可長期使用的操作規則，而不是把所有背景、工作進度、知識、SOP 與一次性需求塞進同一段文字。

支援以下任務：

- 從零建立 Project Instruction
- 診斷現有版本的缺漏、衝突、重複與漂移
- 修訂並交付完整替換版
- 合併已確認的新規則
- 壓縮過長內容，但保留治理邊界
- 比較現行版與建議版
- 判斷內容應放在哪一層
- 評估 Project Instruction 是否真的需要更新

## 核心邊界

先判斷內容的正確承載位置：

- **Project Instruction**：專案目的、成功條件、專案背景、範圍、優先順序、穩定的專案規則、授權邊界、Skill 路由、跨 Skill 順序、專案例外與必要輸出要求。
- **About Me**：跨專案都成立的使用者背景、角色、語言及長期偏好。
- **Global Custom Instructions**：跨專案都適用的 AI 角色、可信原則、一般回應規則與全域工作方式。
- **Skill**：可重複使用的詳細流程、固定 SOP、檢查表、輸出契約與專業方法。
- **一次性 Prompt**：單次任務、當次受眾、期限、特定交付物與臨時限制。
- **Project 來源或 Canonical**：大量事實、正式決策、資料、會議紀錄、版本全文、持續變動的狀態與長期知識。
- **工作計畫或追蹤系統**：待辦、Owner、依賴、里程碑、進度與核准點。

不要因某項內容重要，就自動放進 Project Instruction。只保留會持續影響該 Project 中多數對話的規則。

## 證據與狀態邊界

- 只使用目前可見對話、使用者提供內容、已讀取檔案及工具實際取得資料。
- 不宣稱已讀取整個 Project、其他 Thread、未提供附件、未讀取的 Notion 或其他 AI 記憶。
- 將使用者最新編輯或明確確認的版本視為現行工作版本；不要恢復已被使用者改掉的舊文字。
- 區分現行版、建議版、已套用版與歷史快照。
- 未經使用者陳述或工具驗證，不得宣稱 Project Instruction 已在 UI 生效。
- 遇到矛盾時保留差異並標示「待釐清」，不要自行裁定。
- 若結論依賴目前產品限制、介面、權限或字數上限，查閱最新官方資料；不要把舊限制寫成永久規則。

## 任務模式

先辨識使用者要的是哪一種模式：

1. **Create**：沒有現行版，建立第一版。
2. **Audit**：只檢查問題，不改寫全文。
3. **Revise**：以現行版為基礎，交付完整替換版。
4. **Patch**：只處理明確指定的局部變更。
5. **Merge**：整合多份規則或多次已確認決策。
6. **Compress**：在字數限制內保留必要規則。
7. **Compare**：比較現行版與候選版。
8. **Placement**：判斷某內容是否應進入 Project Instruction。

若使用者說「建立」「更新」「修正」而未另行指定，預設使用 **Revise／Create + 完整可貼上版本**，不要只提供零散建議。

## 執行流程

### Step 1｜建立 Project 基線

確認並標示：

- Project 要解決的問題
- 主要工作與預期成果
- 成功條件與優先順序
- 適用範圍與明確排除項目
- 穩定背景與重要限制
- 使用者、AI、團隊或工具的責任邊界
- 正式內容或 Canonical 的位置
- 已知的字數或格式限制

使用以下狀態：

- 已確認
- 合理推論
- 暫定
- 待確認

只有缺少的資訊會實質改變目的、架構、權限或高風險決策時，才一次詢問一個最重要問題。若可合理前進，先建立暫定版本並標示假設。

若連 Project 真正目的都尚未釐清，先使用 `unknown-pass`；不要用 Project Instruction 掩蓋尚未完成的問題定義。

### Step 2｜執行 Skill Coverage Check

每次建立或修訂 Project Instruction 都要執行：

1. 盤點目前介面可驗證的 Installed Skills。
2. 若目前可存取使用者指定的 Skills Registry，實際讀取最新版；若無法讀取，明確標示「Skills Registry 未讀取」。
3. 必要時讀取相關 `SKILL.md`，確認流程邊界與 exact name。
4. 區分：
   - Registry：治理、版本與狀態真相
   - Installed Skills：目前介面的可用性真相
   - `SKILL.md`：實際流程真相
5. 若三者不一致，標示 `Configuration Drift`，不得自行補造名稱、版本或安裝狀態。
6. 只把專案需要的 Skill 路由、跨 Skill 順序與專案例外寫進 Project Instruction。
7. 不複製 Skill 的完整 SOP、固定輸出格式與品質檢查。

若沒有可驗證的 Skill inventory，仍可先提供暫定版本，但必須標示未驗證範圍，不得假裝完成 Coverage Check。

### Step 3｜診斷現行版本

有現行版時，檢查：

- 是否重複 About Me 或 Global Custom Instructions
- 是否複製已由 Skill 承載的 SOP
- 是否混入一次性 Prompt、待辦、會議紀錄或暫時進度
- 是否把建議、假設或預計執行寫成正式決策
- 是否有互相衝突、重複或無法同時遵守的規則
- 是否含過時產品名稱、功能、權限或介面假設
- 是否宣稱 AI 能讀取其實無法存取的來源
- 是否把 AI 分工寫成產品能力的絕對限制
- 是否缺少專案目的、成功條件、範圍或優先順序
- 是否有無人維護的 Registry、看板、資料庫或流程
- 是否過長、過度工程化或難以在實際對話中遵守

只指出會影響行為、可信度、維護或字數的重要問題。

### Step 4｜決定保留、移動、刪除與新增

將候選內容分為：

- **保留**：長期、專案特有且會影響多數任務。
- **改寫**：方向正確，但語意不清、過度絕對或無法操作。
- **移出**：重要但應放在 Skill、Prompt、Project 來源、Canonical 或工作計畫。
- **刪除**：重複、過時、互相衝突、無人維護或沒有行為效果。
- **新增**：目前缺少且會明顯改善專案工作的必要規則。

不要為了讓結構看起來完整而新增制度、Agent、Skill、資料庫、自動化或 Canonical。

### Step 5｜建立最小充分結構

依 Project 需要選用下列區塊，不必全部套用：

1. 專案目的與成功條件
2. 專案背景、範圍與非目標
3. AI 角色與主要任務
4. 優先順序與決策原則
5. 可信、證據與推論邊界
6. 專案特有工作流
7. Skill 路由與跨 Skill 順序
8. 工具、權限與 Canonical 邊界
9. 輸出與溝通要求
10. Configuration Change、Knowledge Delta 或交班規則

採用清楚、可執行的規則：

- 說明何時觸發
- 說明 AI 應做什麼
- 說明 AI 不應做什麼
- 只有需要時才指定輸入、輸出、Owner、Reviewer 或核准點
- 將例外寫在最接近其適用規則的位置
- 使用 exact Skill names
- 優先寫專案特有差異，不重述全域原則

### Step 6｜交付結果

依任務模式調整輸出。

建立或修訂時，預設依序提供：

1. **可直接貼上的完整版本**
2. **修訂摘要**：只列重要的新增、改寫、移出與刪除
3. **待確認事項**：只列會改變方向的問題
4. **Configuration Delta**：標示為「建議中」或「已確認」，並說明是否需要更新 Snapshot、Setup Log、Architecture、Registry 或其他 Canonical

若使用者只要求 Audit、Compare、Patch 或 Placement，遵照指定模式，不強制重寫全文。

若有字數限制：

- 先保留目的、優先順序、可信邊界、授權範圍與專案例外。
- 再壓縮背景、例子與可由 Skill 承載的細節。
- 不用刪除安全、證據或權限邊界換取字數。
- 回報實際字元數與採用的上限來源；上限未驗證時明確標示。

### Step 7｜完成前驗證

確認：

- 內容確實屬於該 Project，而不是全域個人設定
- Project 目的、成功條件、範圍與優先順序彼此一致
- 沒有把暫時狀態寫成永久規則
- 沒有把討論、建議或候選方案寫成已裁定
- 沒有重複相關 Skill 的完整 SOP
- 所有 Skill 名稱均已驗證或清楚標示未驗證
- 沒有宣稱能存取未讀取的來源
- 沒有互相衝突或無法同時遵守的指令
- 沒有無人維護或無法驗證的新制度
- 產品行為與限制若屬快速變動資訊，已有官方依據或保留查證語句
- 完整版本可直接貼上，沒有殘留編輯註解或不明 placeholder
- 字數符合已知限制
- 未把「建議版」誤寫成「已套用版」

## 與其他 Skills 的邊界

- 使用 `unknown-pass` 處理仍會改變 Project 定義的重大未知。
- 使用 `conversation-review` 先收斂長對話中的決策、矛盾與未解問題；不要假裝已讀整個 Project。
- 使用 `system-design-to-implementation-bridge` 設計新的跨工具系統或工作流；本 Skill 只把已確認的專案規則寫進 Instruction。
- 使用 `skill-creator` 建立或修改實際 Skill；本 Skill 只能指出應移入 Skill 的內容。
- 只有確實由 Claude 接手長文件整合、程式工作、獨立第二意見或其主責文件更新時，才使用 `claude-handoff`。Notion 日常維護預設由 ChatGPT Work 承接，不因涉及正式頁面自動交班；INDEX／CLAUDE.md 檔案操作仍依適用專案指示。
- 只有使用者明確要求保存到 Notion 時，才使用 `notion-capture`。
- 只有結論依賴目前 ChatGPT 功能、限制或操作方式時，才使用 `openai-docs` 查證官方資料。

## Configuration Change 規則

將 Project Instruction 的新增、修訂或移除視為 Configuration Change。

- 草稿完成後，標示為「建議版」，不要宣稱已套用。
- 使用者明確確認 UI 已更新後，才標示為「已套用」。
- 形成最小 Configuration Delta：變更內容、理由、影響範圍、是否需要同步其他正式來源。
- 只建議更新實際受影響的 Snapshot、Setup Log、Architecture、Registry 或 Canonical，不固定全量同步。
- 若需正式落地，先讀取使用者指定的導航入口與受影響頁面。
- 未經明確授權，不直接修改 Notion、Architecture、Registry、Project 設定或其他 Canonical。
- 無法讀取正式來源時，提供待執行清單或 Handoff，不宣稱同步完成。

## 最終品質標準

好的 Project Instruction 應同時做到：

1. 讓 AI 知道這個 Project 要完成什麼。
2. 讓 AI 知道哪些規則是專案特有且長期成立。
3. 讓 AI 不必從大量重複 SOP 中尋找真正優先事項。
4. 讓暫時工作、正式知識、Skill 與全域設定各自留在正確位置。
5. 讓使用者能直接貼上、持續維護、追蹤差異並安全回復。
