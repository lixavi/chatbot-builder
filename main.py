





from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
from rasa.utils.endpoints import EndpointConfig
from rasa.core.channels import ConsoleInputChannel

def run_chatbot():
    interpreter = RasaNLUInterpreter("path/to/nlu_model")
    endpoints = EndpointConfig("http://localhost:5055/webhook")
    agent = Agent.load("path/to/dialogue_model", interpreter=interpreter, action_endpoint=endpoints)

    print("Bot is ready to chat! Type your messages here or 'stop' to end.")

    while True:
        user_input = input()
        if user_input.lower() == 'stop':
            break

        responses = agent.handle_text(user_input)
        for response in responses:
            print(response["text"])

if __name__ == "__main__":
    run_chatbot()





