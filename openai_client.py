import os

from dotenv import load_dotenv
from openai import OpenAI


def load_api_key() -> str:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Add it to your .env file.")
    return api_key


def create_client(api_key: str | None = None) -> OpenAI:
    return OpenAI(api_key=api_key or load_api_key())
