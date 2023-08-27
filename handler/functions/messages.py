import json


def load_messages(filename="messages.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


messages = load_messages()
def get_message_text(keyword: str) -> str:
    return messages.get(keyword, "ごめん、よくわからないかも")

__all__ = ["get_message_text"]