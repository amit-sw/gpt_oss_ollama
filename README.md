# Streamlit Starter

A minimal Streamlit app with configurable logging.

## Ollama
 - Download Ollama from https://ollama.com/download
 - Run `ollama pull gpt-oss:20b`
 - Run `ollama run gpt-oss:20b`


## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## Logging
- Level via env var: `LOG_LEVEL=DEBUG` (default: INFO)
- Optional file output: `LOG_TO_FILE=app.log`

Examples:
```bash
LOG_LEVEL=DEBUG streamlit run app.py
LOG_LEVEL=INFO LOG_TO_FILE=app.log streamlit run app.py
```
