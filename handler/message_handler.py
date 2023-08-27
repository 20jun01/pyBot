from fastapi import Response
from .talk_handler import *
from .response_handler import *
from . import functions


def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
        print("message from bot")
        return Response(status_code=204)

    message_sent = body["message"]["plainText"]
    channel_id = body["message"]["channelId"]
    user = body["message"]["user"]["name"]
    display_name = body["message"]["user"]["displayName"]

    is_personal, prefix, message_truthy = functions.get_message_prefixes(message_sent)
    message_content = ""

    if functions.is_join_prefix(prefix):
        join_channel(channel_id)

    elif functions.is_leave_prefix(prefix):
        leave_channel(channel_id)

    # .replaceはgenerate側の責務な気もするけど、@を返したくないのはtraqへの投稿の責務なのでここでやる
    elif functions.is_talk_prefix(prefix):
        message_content = generate_talk(
            message_truthy, is_personal, False, user).replace("@", "`@`")

    elif functions.is_talk_cont_prefix(prefix):
        message_content = generate_talk(
            message_truthy, is_personal, True, user).replace("@", "`@`")

    elif functions.is_add_setting_prefix(prefix):
        add_system_settings(message_truthy, is_personal, user)

    elif functions.is_new_setting_prefix(prefix):
        new_system_settings(message_truthy, is_personal, user)

    elif functions.is_del_setting_prefix(prefix):
        new_system_settings("", is_personal, user)

    elif functions.is_show_setting_prefix(prefix):
        message_content = "`" + get_system_settings(is_personal, user) + "`"

    # TODO: prefixを受け取った後の処理をする関数は別に作る(つまり、ここではget_message_textはしない)
    message = create_response_message(prefix, message_content)
    post_to_traq(message, channel_id)
    return Response(status_code=204)


def create_response_message(message_type: str) -> str:
    return functions.get_message_text(message_type)


__all__ = ["message_created_response"]
