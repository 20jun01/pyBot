import json
import os


# template({})を含めてキーワードで置き換える
# def load_templates(filename="templates.json"):
#     with open(filename, 'r', encoding='utf-8') as file:
#         return json.load(file)

# templates = load_templates()

# def format_template(template_key, **kwargs):
#     template = templates.get(template_key, "")
#     return template.format(**kwargs)

# # 使用例
# message = format_template("greeting", name="Alice")
# print(message)  # 出力: Hello, Alice!


COMMAND_PREFIXES = ['help', '@BOT_urturn_Talker /join',
                    '/leave', '/cont', '/add', '/new', '/del', '/show']
COMMAND_PREFIXES_PERSONAL = ['/personal cont', '/personal add',
                             '/personal new', '/personal del', '/personal show', '/personal']


def get_message_prefixes_personal(message_sent: str) -> (bool, str, str):
    for prefix in COMMAND_PREFIXES_PERSONAL:
        if message_sent.startswith(prefix):
            return True, prefix.replace("/personal", "").strip(), message_sent.replace(prefix, "")
    return False, ""


def get_message_prefixes(message_sent: str) -> (str, str):
    for prefix in COMMAND_PREFIXES:
        if message_sent.startswith(prefix):
            return prefix.replace("/", ""), message_sent.replace(prefix, "")
    return "", message_sent


# TODO: 辞書型にしてもう少し綺麗にしたい
def is_join_prefix(prefix) -> bool:
    return prefix == "@BOT_urturn_Talker /join".replace("/", "")


def is_leave_prefix(prefix) -> bool:
    return prefix == "/leave".replace("/", "")

def is_talk_prefix(prefix: str) -> bool:
    return prefix == ""

def is_talk_cont_prefix(prefix: str) -> bool:
    return "cont" in prefix

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


__all__ = ["get_message_text", "get_message_prefixes",
           "get_message_prefixes_personal", "is_join_prefix", "is_leave_prefix", "is_talk_prefix", "is_talk_cont_prefix"]
