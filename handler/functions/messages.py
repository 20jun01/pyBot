import json
import os


# TODO: fix path with relative
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "messages.json")
def load_messages(filename: str = FILE_PATH):
    print(os.getcwd())
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


messages = load_messages()
def get_message_text(keyword: str) -> str:
    return messages.get(keyword, "ごめん、よくわからないかも")

__all__ = ["get_message_text"]