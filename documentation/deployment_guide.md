# Deployment Guide

## Local Run
1. Create and activate a virtual environment.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the app: `streamlit run app.py`.

## Configuration
- `LOG_LEVEL`: DEBUG, INFO, WARNING, ERROR (default: INFO)
- `LOG_TO_FILE`: Optional file path for logs; if unset, logs go to console.

## Notes
- Tested with Python 3.10+ on macOS.
- Pin updates: adjust `requirements.txt` and retest locally.
