from .functions import open_ai

system_settings = ""

personal_settings = {}

personal_past_messages = {}

with open("system_setting.txt", "r") as f:
    system_settings = f.read()

past_message = []


def generate_talk(message: str, is_personal: bool, is_cont: bool, user: str = "") -> str:
    global past_messages, personal_past_messages
    if is_personal:
        past_messages = personal_past_messages.get(user, []) if is_cont else []
        new_message, messages = talk_handler_personal(
            past_messages, message, user)
        personal_past_messages[user] = messages
    else:
        past_messages = past_messages if is_cont else []
        new_message, messages = talk_handler(past_messages, message)
        past_messages = messages
    return new_message


def talk_handler(past_messages: str, message: str):
    new_message, messages = open_ai.completion(
        message, system_settings, past_messages)
    return new_message, messages


def add_system_settings(settings: str, is_personal: bool, user: str = ""):
    global system_settings
    if is_personal:
        personal_settings[user] = personal_settings.get(user, "") + settings
        return
    system_settings += settings
    with open("system_setting.txt", "w") as f:
        f.write(system_settings)


def get_system_settings(is_personal: bool, user: str = "") -> str:
    global system_settings
    return personal_settings.get(user, '') if is_personal else system_settings


def new_system_settings(settings: str, is_personal: bool, user: str = ""):
    global system_settings, personal_settings
    if is_personal:
        personal_settings[user] = settings
        return
    system_settings = settings
    with open("system_setting.txt", "w") as f:
        f.write(system_settings)


def talk_handler_personal(past_messages: str, message: str, user: str):
    global personal_settings
    new_message, messages = open_ai.completion(
        message, personal_settings.get(user, ""), past_messages)
    return new_message, messages


__all__ = ["generate_talk", "add_system_settings", "new_system_settings", "add_settings_personal",
           "new_settings_personal", "get_system_settings"]
