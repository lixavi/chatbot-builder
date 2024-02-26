# Chatbot Builder

Chatbot Builder is a Python-based program that leverages Rasa NLU for natural language understanding and custom intent recognition. It provides an environment for training a chatbot to understand and respond to user messages effectively.

## Features

- Utilizes Rasa NLU for natural language understanding.
- Supports custom intent recognition for handling specialized user queries.
- Provides a training environment for building and fine-tuning chatbot models.
- Modular architecture with separate components for easier management and extension.

## Getting Started

To get started with Chatbot Builder, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Train the Rasa NLU and dialogue models using the provided training data (`nlu.md` and `stories.md`).
4. Customize the chatbot's behavior by editing the domain file (`domain.yml`) and adding custom actions (`actions.py`).
5. Run the chatbot using `python main.py` and start interacting with it through the console.
