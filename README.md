# OpenAI API Python Demo

This project is a small Python demo for calling the OpenAI API. It is based on the roadmap.sh project idea:

https://roadmap.sh/projects/openai-api-python

The original all-in-one walkthrough lives in `demo_all_in_one.ipynb`. The main `demo_capsulated.ipynb` imports the standalone Python files so each example can be demonstrated without duplicating the implementation.

## Project Files

- `demo_all_in_one.ipynb`: Original all-in-one notebook demo for quick reference.
- `demo_capsulated.ipynb`: Notebook demo that imports the standalone Python modules.
- `openai_client.py`: Shared helper for loading `OPENAI_API_KEY` and creating an OpenAI client.
- `simple_call.py`: Makes one chat completion request.
- `temperature_demo.py`: Compares responses with different `temperature` values.
- `chat_with_history.py`: Runs an interactive chat loop with conversation history.
- `.env.example`: Template for local environment variables.
- `requirements.txt`: Python dependencies.

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Create your local `.env` file:

```powershell
Copy-Item .env.example .env
```

Then edit `.env` and add your API key:

```text
OPENAI_API_KEY=your_api_key_here
```

## Run Examples

Run a single API call:

```powershell
python simple_call.py
```

Compare temperature values:

```powershell
python temperature_demo.py
```

Start an interactive chat with history:

```powershell
python chat_with_history.py
```

In the interactive chat, type `clear` to clear chat history, or `quit`, `exit`, `bye`, or `stop` to end the session.

## Notes

Do not commit your real `.env` file or API key. This repository includes `.env.example` only as a safe template.
