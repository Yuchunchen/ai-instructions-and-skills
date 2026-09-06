# 工具模式與配置

本檔是按情境選用的參考。依 SKILL.md 已選模式、實際風險與使用者要求挑選相關段落；沒有相關問題時可明說未發現，不為數量或格式新增問題、產物或核准。

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

### Mode D｜ChatGPT Work／Claude Cowork 執行

適合：

* 架構已明確
* 需要多步驟檔案或知識工作
* 日常 Notion 整理、Architecture 或 Registry 維護，預設由 ChatGPT Work 承接
* Claude 主責的長文件或程式工作，可由其可用介面更新對應 Notion 頁面

先指定本次主責 AI，確認工具、授權與回讀方式；INDEX／CLAUDE.md 檔案操作沿用適用專案指示。

### Mode E｜Claude Code／Codex 技術實作

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
* 多來源資料整理與日常 Notion 維護；在授權範圍內更新受影響頁面並回讀

不適合：

* 取代未完成的策略與架構討論

## Claude Code／Codex

程式工作預設考慮 Claude／Claude Code；Codex 可依使用者指定或既有執行環境承接。

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
* 主責長文件的正式稿與版本一致性
* 使用者需要時提供獨立第二意見；不作為所有工作的必經核准

需要注意：

* 只接收已定案或清楚標示暫定的內容
* 不自行改變策略

## Claude Cowork

適合：

* 按 Implementation Plan 修改正式文件
* 管理多步驟落地工作
* 完成主責長文件或程式工作時，更新已授權的對應 Notion 頁面並回讀；日常 Notion 維護預設由 ChatGPT Work 承接
* 既有 INDEX／CLAUDE.md 檔案工作依專案專屬流程

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
