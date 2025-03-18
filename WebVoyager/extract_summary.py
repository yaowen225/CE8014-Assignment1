import os
import json
import re
from datetime import datetime

def extract_summary_from_json(json_file):
    """從interact_messages.json提取ANSWER內容"""
    with open(json_file, 'r', encoding='utf-8') as f:
        messages = json.load(f)
    
    for message in messages:
        if message['role'] == 'assistant' and 'content' in message:
            # 檢查是否包含"Action: ANSWER;"字串
            if 'Action: ANSWER;' in message['content']:
                # 提取ANSWER後的內容
                answer_part = message['content'].split('Action: ANSWER;')[1].strip()
                return answer_part
    
    # 如果沒有找到Answer，檢查最後一條消息是否表示無法完成任務
    if messages and messages[-1]['role'] == 'assistant' and 'content' in messages[-1]:
        last_msg = messages[-1]['content']
        if "unable to assist" in last_msg.lower() or "cannot complete" in last_msg.lower():
            return "**⚠️ 任務未能完成** - 代理在爬取過程中遇到了困難，可能是因為:\n\n1. 找不到相關新聞，因這方面的新聞本身就容易較少\n2. 網站結構可能已經變化\n3. 連接問題或超時\n\n建議手動檢查網站或調整任務參數後再試。"
    
    return None

def main():
    # 獲取最新結果目錄
    results_dir = './results'
    latest_dir = None
    latest_time = 0
    
    for dirname in os.listdir(results_dir):
        if os.path.isdir(os.path.join(results_dir, dirname)) and dirname != 'examples':
            dir_path = os.path.join(results_dir, dirname)
            dir_time = os.path.getmtime(dir_path)
            if dir_time > latest_time:
                latest_time = dir_time
                latest_dir = dirname
    
    if not latest_dir:
        print("找不到結果目錄")
        return
    
    # 創建摘要MD文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f'./esg_summary_{timestamp}.md'
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# ESG新聞摘要報告\n\n")
        f.write(f"生成時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        latest_result_path = os.path.join(results_dir, latest_dir)
        
        # 處理每個任務目錄
        for task_dir in os.listdir(latest_result_path):
            task_path = os.path.join(latest_result_path, task_dir)
            if os.path.isdir(task_path):
                # 提取任務類型 (Environment, Social, Governance)
                task_type = "未知類型"
                if "Environment" in task_dir:
                    task_type = "環境 (Environmental)"
                elif "Social" in task_dir:
                    task_type = "社會 (Social)"
                elif "Governance" in task_dir:
                    task_type = "治理 (Governance)"
                
                f.write(f"## {task_type}新聞摘要\n\n")
                
                # 讀取json文件
                json_file = os.path.join(task_path, 'interact_messages.json')
                if os.path.exists(json_file):
                    summary = extract_summary_from_json(json_file)
                    if summary:
                        f.write(f"{summary}\n\n")
                    else:
                        f.write("未找到摘要結果\n\n")
                else:
                    f.write("未找到互動訊息文件\n\n")
    
    print(f"摘要已保存至 {output_file}")

if __name__ == "__main__":
    main() 