## System Requirements

- Python 3.10
- Chrome Browser (latest version)
- Anaconda (recommended)
- Stable internet connection

## Environment Setup

1. Create and activate Anaconda environment:
```bash
conda create -n webvoyager python=3.10
conda activate webvoyager
```

2. Install required packages:
```bash
pip install openai==1.1.1 selenium==4.15.2 pillow==10.1.0
```

3. Configure OpenAI API:
```bash
# Windows
set OPENAI_API_KEY=your_api_key_here

# Linux/Mac
export OPENAI_API_KEY=your_api_key_here
```

## Execution Parameters

Main command line arguments (as shown in howtorun.md):
```bash
python -u run.py \
  --test_file ./data/tasks_test.jsonl \
  --api_key OPENAI_API_KEY \
  --api_model gpt-4o \
  --max_iter 20 \
  --max_attached_imgs 3 \
  --temperature 1 \
  --window_width 1920 \
  --window_height 1080 \
  --fix_box_color \
  --force_device_scale \
  --seed 42
```

Additional parameters:
- `--headless`: Run in headless mode
- `--save-accessibility-tree`: Save accessibility tree for analysis

## how to run

1. add your api key to "run_and_extract.bat" file.
2. open cmd and type(remember to replace the path):
```bash
cd "your_file_path\Assignment 1_113922002\all project file\WebVoyager"

run_and_extract.bat
```

## Output Files

- ESG Summaries: `esg_summary_[timestamp].md`
- Execution Logs: `agent.log`
- Crawling Results: `results/` directory 