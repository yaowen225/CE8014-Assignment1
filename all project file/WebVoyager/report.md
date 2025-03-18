Assignment 1: 
Reflexive Web Agent with Tools Use
Student ID: 123456789, Name: Your_Name

1.	(10%) Describe your Agentic AI application scenario, including target users, use cases, and problems to be solved.
(Provide a comprehensive description of your application with at least 2-3 specific use cases, clearly defined target users, and concrete problems to be solved.)

[English Version]
This project develops an automated ESG (Environmental, Social, and Governance) news crawling and summarization system based on the WebVoyager framework.

Target Users:
- ESG risk assessment teams in investment institutions
- ESG analysts and researchers
- Corporate sustainability department personnel
- General investors interested in ESG issues

Use Cases:
1. Automated ESG News Monitoring
   - Automatically browse ESG news websites
   - Identify and categorize latest news in environmental, social, and governance aspects
   - Generate structured Chinese summary reports
   
2. ESG Trend Analysis Support
   - Continuously track ESG-related news for specific companies or industries
   - Analyze news impact on sustainable development
   - Help decision-makers quickly grasp ESG development trends

3. Cross-language ESG Information Integration
   - Automatically translate English ESG news into Chinese summaries
   - Standardize output format for subsequent analysis
   - Reduce language barriers in information acquisition

Problems to be Solved:
1. ESG news information is scattered, and current collection methods need improvement as they are time-consuming and labor-intensive.
2. When considering multiple news sources in the future, significant variations between different news content may make systematic analysis difficult.
3. To transform news into actionable decision-making advice, additional methods need to be considered to ensure proper impact assessment.

[中文版本]
本專案開發了一個自動化的ESG（環境、社會、治理）新聞爬取與摘要系統，基於WebVoyager框架進行改造。

target users：
- 投資機構的ESG風險評估團隊
- ESG分析師和研究人員
- 企業永續發展部門人員
- 對ESG議題感興趣的一般投資者

使用情境：
1. 自動化ESG新聞監控
   - 系統自動瀏覽ESG新聞網站
   - 識別並分類環境、社會、治理三大面向的最新新聞
   - 生成結構化的中文摘要報告
   
2. ESG趨勢分析支援
   - 持續追蹤特定企業或產業的ESG相關新聞
   - 分析新聞對永續發展的影響
   - 協助決策者快速掌握ESG發展動態

3. 跨語言ESG資訊整合
   - 自動將英文ESG新聞翻譯成中文摘要
   - 統一格式化輸出，便於後續分析
   - 降低語言障礙對資訊獲取的影響

待解決問題：
1. ESG新聞資訊分散，且目前的搜集方法還有待加強，收集耗時費力，有優化空間。
2. 若未來考慮多個新聞來源，不同新聞內容間可能存在大量差異，不易進行系統性分析，需要再考慮如何調整一致性。
3. 若想從新聞再進一步變成能夠給予決策上的建議，需要再考慮增加其他方法來確保能正確地轉化成影響力。

2.	(10%) Analyze at least 2 potential technical challenges in implementation and propose preliminary solutions.
(For each technical challenge, provide detailed analysis including impact assessment and step-by-step solution proposals with feasibility evaluation.)

[English Version]
Technical Challenge 1: Web Element Location and Interaction

Impact Assessment:
- WebVoyager framework requires precise element location
- Dynamic loading characteristics of ESG News website
- News content distributed across different page levels

Solutions:
1. Optimize Element Location Strategy
   - Implement digital labeling system
   - Use multi-level selectors
   - Add waiting mechanisms for dynamic loading

2. Error Handling Mechanism
   - Implement error detection in extract_summary.py
   - Provide clear error messages
   - Log interaction process for debugging

Feasibility Assessment:
- Verified implementable through WebVoyager framework
- Error handling mechanism working well
- Maintenance costs currently acceptable

Technical Challenge 2: Multilingual Content Processing and Conversion

Impact Assessment:
- Original news in English
- High difficulty in translating ESG terminology
- Need to maintain output format consistency

Solutions:
1. Prompt Optimization
   - Explicitly require Chinese output in tasks_test.jsonl
   - Add translation guidelines in prompts.py
   - Standardize summary format specifications

2. Summary Extraction Improvements
   - Develop extract_summary.py script
   - Implement unified output format
   - Automatically generate MD reports

Feasibility Assessment:
- Successfully implemented Chinese summary generation
- Unified and readable format
- Can continuously optimize translation quality

[中文版本]
技術挑戰一：網頁元素定位與互動

影響評估：
- WebVoyager框架需要準確定位元素
- ESG News網站的動態加載特性
- 新聞內容分散在不同頁面層級

解決方案：
1. 優化元素定位策略
   - 實作數字標籤系統
   - 使用多層次的選擇器
   - 添加等待機制處理動態加載

2. 錯誤處理機制
   - 在extract_summary.py中實作錯誤檢測
   - 提供清晰的錯誤提示
   - 記錄互動過程便於除錯

可行性評估：
- 已驗證可透過WebVoyager框架實現
- 錯誤處理機制運作良好
- 維護成本目前在可接受範圍

技術挑戰二：多語言內容處理和轉換

影響評估：
- 原始新聞為英文
- ESG專業術語翻譯難度高
- 需要保持輸出格式一致性

解決方案：
1. 提示詞優化
   - 在tasks_test.jsonl中明確要求中文輸出
   - 在prompts.py添加翻譯指南
   - 統一摘要格式規範

2. 摘要提取改進
   - 開發extract_summary.py腳本
   - 實作統一的輸出格式
   - 自動生成MD報告

可行性評估：
- 已成功實現中文摘要生成
- 格式統一且易於閱讀
- 可持續優化翻譯品質

3.	(20%) Explain how your system implements the complete cycle of environment perception, decision making, and action execution.
(Detail the complete workflow of your system, demonstrating how each component interacts within the perception-brain-action cycle.)

[English Version]
Based on the WebVoyager framework, our system implements a complete perception-decision-action cycle:

1. Environment Perception
   - Webpage State Capture
     * Use WebVoyager's screenshot functionality
     * Identify page element locations
     * Parse DOM structure
   
   - Content Analysis
     * Based on tasks defined in tasks_test.jsonl
     * Identify ESG-related news
     * Determine news category and importance

2. Decision Making
   - Task Planning
     * Parse ESG guidelines from prompts.py
     * Select appropriate news articles
     * Determine reading and summary strategy
   
   - Interaction Decisions
     * Determine if page scrolling is needed
     * Select click targets
     * Decide whether to generate summary

3. Action Execution
   - Web Operations
     * Execute WebVoyager framework interaction commands
     * Handle page responses
     * Wait for content loading
   
   - Result Output
     * Call extract_summary.py
     * Generate structured summaries
     * Output MD format reports

4. Feedback Processing
   - Execution Monitoring
     * Record operation results
     * Monitor execution status
     * Handle exceptional situations
   - Result Validation
     * Confirm summary completeness
     * Verify Chinese output
     * Check format specifications

[中文版本]
基於WebVoyager框架，本系統實現了完整的感知-決策-行動循環：

1. 環境感知 (Perception)
   - 網頁狀態捕獲
     * 使用WebVoyager的截圖功能
     * 識別頁面元素位置
     * 解析DOM結構
   
   - 內容分析
     * 根據tasks_test.jsonl定義的任務
     * 識別ESG相關新聞
     * 判斷新聞類別和重要性

2. 決策制定 (Decision Making)
   - 任務規劃
     * 解析prompts.py中的ESG指南
     * 選擇合適的新聞文章
     * 確定閱讀和摘要策略
   
   - 互動決策
     * 判斷是否需要滾動頁面
     * 選擇點擊目標
     * 決定是否生成摘要

3. 行動執行 (Action)
   - 網頁操作
     * 執行WebVoyager框架的互動命令
     * 處理頁面響應
     * 等待內容加載
   
   - 結果輸出
     * 調用extract_summary.py
     * 生成結構化摘要
     * 輸出MD格式報告

4. 反饋處理
   - 執行監控
     * 記錄操作結果
     * 檢測執行狀態
     * 處理異常情況
   - 結果驗證
     * 確認摘要完整性
     * 驗證中文輸出
     * 檢查格式規範

4.	(30%) Design and execute 3 test tasks, analyze the results, and propose potential improvements based on the current implementation.
(Document the execution of three test cases with comprehensive analysis of results and specific improvement suggestions.)

[English Version]
Test Task Design:
Based on tasks_test.jsonl configuration, execute three ESG news crawling tasks:

1. Environmental News Test (ESG News-Environment-1)
   Execution Results:
   - Successfully retrieved Neste green bond news
   - Completed title and date extraction
   - Initial execution produced English summaries
   
   Improvements:
   - Modified tasks_test.jsonl to add Chinese requirements
   - Updated ESG guidelines in prompts.py
   - Refined summary format specifications

2. Social News Test (ESG News-Social-1)
   Execution Results:
   - Successfully retrieved DEI weekly news
   - Correctly generated Chinese summaries
   - Format met requirements
   
   Improvements:
   - Optimize social issue keywords
   - Improve news classification logic
   - Enhance timeliness judgment

3. Governance News Test (ESG News-Governance-1)
   Execution Results:
   - Encountered difficulties in news retrieval
   - extract_summary.py provided error messages
   - Recorded failure reasons
   
   Improvements:
   - Expand governance news keywords
   - Optimize search strategies
   - Add retry mechanisms

Implementation Improvement Focus:

1. Program Structure
   - Added extract_summary.py for summary processing
   - Created run_and_extract.bat for one-click execution
   - Optimized error handling mechanisms

2. User Interface
   - Unified MD output format
   - Added execution status indicators
   - Improved error message display

3. Stability Enhancement
   - Improved webpage waiting mechanism
   - Enhanced element location strategy
   - Strengthened exception handling

4. Future Optimizations
   - Support for more news sources
   - Implement batch processing functionality
   - Add database storage

[中文版本]
測試任務設計：
基於tasks_test.jsonl配置，執行三個ESG新聞爬取任務：

1. 環境新聞測試 (ESG News-Environment-1)
   執行結果：
   - 成功抓取Neste綠色債券新聞
   - 完成標題和日期提取
   - 初次執行出現英文摘要
   
   改進措施：
   - 修改tasks_test.jsonl添加中文要求
   - 更新prompts.py的ESG指南
   - 完善摘要格式規範

2. 社會新聞測試 (ESG News-Social-1)
   執行結果：
   - 成功抓取DEI週報新聞
   - 正確生成中文摘要
   - 格式符合要求
   
   改進措施：
   - 優化社會議題關鍵詞
   - 改進新聞分類邏輯
   - 加強時效性判斷

3. 治理新聞測試 (ESG News-Governance-1)
   執行結果：
   - 遇到新聞查找困難
   - extract_summary.py提供錯誤提示
   - 記錄了失敗原因
   
   改進措施：
   - 擴充治理新聞關鍵詞
   - 優化搜索策略
   - 添加重試機制

實作改進重點：

1. 程式架構
   - 新增extract_summary.py處理摘要
   - 創建run_and_extract.bat實現一鍵執行
   - 優化錯誤處理機制

2. 使用者介面
   - 統一MD輸出格式
   - 添加執行狀態提示
   - 優化錯誤訊息顯示

3. 穩定性提升
   - 完善網頁等待機制
   - 改進元素定位策略
   - 強化異常處理

4. 後續優化
   - 支援更多新聞來源
   - 實現批次處理功能
   - 添加資料庫儲存



