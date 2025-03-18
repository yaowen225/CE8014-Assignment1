@echo off
echo ===== ESG新聞爬取與摘要系統 =====
echo 正在執行WebVoyager ESG新聞爬取任務...

python -u run.py ^
    --test_file ./data/tasks_test.jsonl ^
    --api_key  ^
    --api_model gpt-4o ^
    --max_iter 20 ^
    --max_attached_imgs 3 ^
    --temperature 1 ^
    --window_width 1920 ^
    --window_height 1080 ^
    --fix_box_color ^
    --force_device_scale ^
    --seed 42

echo 任務完成，正在等待文件系統同步...
timeout /t 3 /nobreak > nul

echo 正在生成ESG新聞摘要報告...
python extract_summary.py

echo 全部完成！
echo 摘要報告已生成，請查看當前目錄下的esg_summary_*.md文件。
echo.
pause 