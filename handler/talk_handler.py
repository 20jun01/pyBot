from ..functions import completion

def talk_handler(past_messages: str, message: str, system_settings: str) -> tuple(str, list[dict(str, str)]):
    new_message, messages = completion(message, system_settings, past_messages)
    past_messages = messages
    return new_message, messages