#!/bin/bash

# 執行WebVoyager任務
echo "正在執行WebVoyager ESG新聞爬取任務..."
python -u run.py \
    --test_file ./data/tasks_test.jsonl \
    --api_key \
    --api_model gpt-4o \
    --max_iter 20 \
    --max_attached_imgs 3 \
    --temperature 1 \
    --window_width 1920 \
    --window_height 1080 \
    --fix_box_color \
    --force_device_scale \
    --seed 42

# 等待3秒確保所有文件都已寫入
echo "任務完成，正在等待文件系統同步..."
sleep 3

# 執行摘要提取腳本
echo "正在生成ESG新聞摘要報告..."
python extract_summary.py

echo "全部完成！" 