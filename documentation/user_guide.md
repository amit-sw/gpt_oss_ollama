# User Guide

## Start the App
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Use the App
- Enter your name in the input field.
- The app displays a greeting when a name is provided.

## Logging
- Default level: INFO
- Enable debug logs:
```bash
LOG_LEVEL=DEBUG streamlit run app.py
```
- Write logs to a file:
```bash
LOG_LEVEL=INFO LOG_TO_FILE=app.log streamlit run app.py
```
