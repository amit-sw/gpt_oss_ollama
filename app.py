import os
import sys
import logging
import streamlit as st
import requests
from openai import OpenAI
import threading
import time

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
    return response


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
        placeholder = st.empty()
        timer_placeholder = st.empty()
        response_container = {}

        def fetch_response():
            response_container['response'] = get_ollama_response(question)

        thread = threading.Thread(target=fetch_response)
        start_time = time.time()
        thread.start()
        while thread.is_alive():
            elapsed = time.time() - start_time
            timer_placeholder.info(f"Thinking... {elapsed:.1f}s")
            time.sleep(0.1)
        thread.join()
        total_time = time.time() - start_time
        timer_placeholder.info(f"Thought for {total_time:.1f}s")

        try:
            response = response_container.get('response')
            if response:
                content = response.choices[0].message.content
                placeholder.success(f"AI says: {content}")
                tokens = getattr(response.usage, 'total_tokens', None)
                if tokens is not None:
                    token_rate = tokens / total_time if total_time > 0 else float('inf')
                    st.caption(f"Time: {total_time:.2f}s | Token rate: {token_rate:.2f} tokens/s")
                else:
                    st.caption(f"Time: {total_time:.2f}s")
            else:
                st.error("No response received from the model.")
        except Exception as e:
            logger.error(f"ollama_error: {e}")
            st.error("Could not get a response from Ollama. Ensure the Ollama server is running and the model is available.")
    else:
        st.info("Enter a question to query the local model via Ollama.")


if __name__ == "__main__":
    main()
