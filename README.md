# Terminal Chatbot

A simple command-line chatbot built with Python and the Hugging Face Inference API. It allows users to send messages and receive AI-generated responses directly in the terminal.

## Features

- Interactive command-line conversation
- AI-generated responses using a hosted language model
- Conversation history maintained during the session
- Environment-based API token configuration
- Simple and lightweight implementation

## Requirements

- Python 3.10+
- A Hugging Face account with access to an available Inference Provider and sufficient credits

## Installation

Clone the repository:

```bash
git clone https://github.com/MohsenRahbar/terminal-chatbot.git
cd terminal-chatbot
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install huggingface_hub python-dotenv
```

## Configuration

Create a `.env` file in the project root:

```env
HF_TOKEN=your_hugging_face_token
```

Replace `your_hugging_face_token` with your Hugging Face access token.

**Important:** Never commit your `.env` file or expose your API token publicly.

Make sure `.env` is included in `.gitignore`.

## Usage

Run the chatbot:

```bash
python chatbot.py
```

Enter a message when prompted. Type `exit` to end the conversation.

## Model

The current implementation uses `openai/gpt-oss-120b` through the Hugging Face Inference API. Model availability and usage may depend on provider access and account credits.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.