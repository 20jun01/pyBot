from .functions import open_ai

system_settings = ""

personal_settings = {}

personal_past_messages = {}

with open("system_setting.txt", "r") as f:
    system_settings = f.read()

past_message = []

def generate_talk(message: str) -> str:
    global past_messages
    new_message, messages = talk_handler([], message)
    past_messages = messages
    return new_message

def generate_talk_cont(message: str) -> str:
    global past_messages
    new_message, messages = talk_handler(past_messages, message)
    past_messages = messages
    return new_message

def talk_handler(past_messages: str, message: str):
    new_message, messages = open_ai.completion(message, system_settings, past_messages)
    return new_message, messages

def add_system_settings(settings: str):
    global system_settings
    system_settings += settings
    with open("system_setting.txt", "w") as f:
        f.write(system_settings)
    
def new_system_settings(settings: str):
    global system_settings
    system_settings = settings
    with open("system_setting.txt", "w") as f:
        f.write(system_settings)

def add_settings_personal(settings: str, user: str):
    global personal_settings
    if user in personal_settings:
        personal_settings[user] += settings
    else:
        personal_settings[user] = settings
    
def new_settings_personal(settings: str, user: str):
    global personal_settings
    personal_settings[user] = settings

def generate_talk_personal(message: str, user: str) -> str:
    global personal_past_messages
    if user in personal_past_messages:
        new_message, messages = talk_handler_personal(personal_past_messages[user], message, user)
        personal_past_messages[user] = messages
    else:
        new_message, messages = talk_handler_personal([], message, user)
        personal_past_messages[user] = messages
    return new_message

def generate_talk_cont_personal(message: str, user: str) -> str:
    global personal_past_messages
    if user in personal_past_messages:
        new_message, messages = talk_handler_personal(personal_past_messages[user], message, user)
        personal_past_messages[user] = messages
    else:
        new_message, messages = talk_handler_personal([], message, user)
        personal_past_messages[user] = messages
    return new_message

def talk_handler_personal(past_messages: str, message: str, user: str):
    global personal_settings
    if user in personal_settings:
        new_message, messages = open_ai.completion(message, personal_settings[user], past_messages)
    else:
        new_message, messages = open_ai.completion(message, system_settings, past_messages)
    return new_message, messages

def settings_personal(user: str) -> str:
    global personal_settings
    if user in personal_settings:
        return personal_settings[user]
    else:
        return ""
