from .functions import open_ai


def talk_handler(past_messages: str, message: str, system_settings: str):
    new_message, messages = open_ai.completion(
        message, system_settings, past_messages)
    past_messages = messages
    return tuple(new_message, messages)
