Here is a concise README draft for your project, including a Python section with step-by-step instructions.

# Multilingual CLI Chatbot

A simple CLI chatbot supporting multiple programming languages (currently Python; Go and Rust planned) and various AI models (OpenAI, Anthropic, Gemini, etc.).

## Features

- CLI interface for interactive chat
- Pluggable language and model support
- Conversation context preservation

## Supported Languages

- Python (available)
- Go (planned)
- Rust (planned)

## Supported Models

- OpenAI (GPT)
- Anthropic (planned)
- Gemini (planned)

---

## Python Quickstart

### 1. Clone the repository

```
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and activate a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Configure environment variables

Add `src/python/.env` and set:

- `OPENAI_API_KEY` — your OpenAI API key
- `OPENAI_MODEL` — model name (e.g., `gpt-4.1-nano`)

### 5. Run the chatbot

```
python src/python/main.py --env-file=.env --log-level=WARNING
```

---

## Logger Configuration

You can set the logging level via environment variable or config:

- Supported levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`
- Example: `LOG_LEVEL=DEBUG`

The logger reads the level from config and falls back to `INFO` if invalid.

---

## Environment Variables

- `OPENAI_API_KEY` — API key for OpenAI
- `OPENAI_MODEL` — model name
- `LOG_LEVEL` — logging level (optional)
