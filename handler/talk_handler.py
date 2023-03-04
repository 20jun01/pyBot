from .functions import open_ai

with open("system_setting.txt", "r") as f:
    system_settings = f.read()

past_message = []

def generate_talk(message: str) -> str:
    global past_messages
    new_message, message = talk_handler([], message)
    past_messages = message
    return new_message

def generate_talk_cont(message: str) -> str:
    global past_messages
    new_message, _ = talk_handler(past_messages, message)
    past_messages = message
    return new_message

def talk_handler(past_messages: str, message: str):
    new_message, messages = open_ai.completion(message, system_settings, past_messages)
    return new_message, messages
