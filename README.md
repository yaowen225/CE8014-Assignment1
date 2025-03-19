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

## How To Run

1. Add your api key to "run_and_extract.bat" file.
2. Open cmd and type(remember to replace the path):
```bash
cd "your_file_path\Assignment 1_113922002\all project file\WebVoyager"

run_and_extract.bat
```

## Output Files

- ESG Summaries: `esg_summary_[timestamp].md`
- Execution Logs: `agent.log`
- Crawling Results: `results/` directory 