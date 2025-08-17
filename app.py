import os
import sys
import logging
import streamlit as st
import requests
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",  # Ollama's default API endpoint
    api_key="ollama"                        # Dummy key, not used by Ollama
)




def configure_logging():
    level = os.getenv("LOG_LEVEL", "INFO").upper()
    level_value = getattr(logging, level, logging.INFO)
    handlers = [logging.StreamHandler(sys.stdout)]
    log_to_file = os.getenv("LOG_TO_FILE")
    if log_to_file:
        handlers.append(logging.FileHandler(log_to_file))
    logging.basicConfig(level=level_value, format="%(asctime)s %(levelname)s %(message)s", handlers=handlers)
    logging.getLogger("streamlit").setLevel(logging.WARNING)

def get_ollama_response(prompt):
    logger = logging.getLogger("app")
    response = client.chat.completions.create(
        model="gpt-oss:20b",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    logger.info(f"ollama_generate_ok: {response.choices[0]}")

    print(response.choices[0].message.content)
    return response.choices[0].message.content


def main():
    configure_logging()
    logger = logging.getLogger("app")
    logger.info("app_start")

    st.set_page_config(page_title="Streamlit Starter", page_icon="🎈", layout="centered")
    st.title("Streamlit Starter")
    st.write("A minimal Streamlit app with configurable logging.")

    question = st.text_input("What is your question?", placeholder="What is the capital of France?")
    if question:
        st.info(f"Question: {question}")
        try:
            response = get_ollama_response(question)
            st.success(f"AI says: {response}")
        except Exception as e:
            logger.error(f"ollama_error: {e}")
            st.error("Could not get a response from Ollama. Ensure the Ollama server is running and the model is available.")
    else:
        st.info("Enter a question to query the local model via Ollama.")


if __name__ == "__main__":
    main()
