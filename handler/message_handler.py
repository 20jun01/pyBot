from fastapi import Response
from .talk_handler import *
from .response_handler import *
from functions import get_message_text


def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
        print("message from bot")
        return Response(status_code=204)

    message_sent = body["message"]["plainText"]

    if message_sent.startswith("/help"):
        message = create_response_message("help")
        post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("@BOT_urturn_Talker /join"):
        join_channel(body["message"]["channelId"])
        message = create_response_message("join")
        post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/leave"):
        leave_channel(body["message"]["channelId"])
        message = create_response_message("leave")
        post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/cont"):
        message_sent = message_sent.replace("/cont", "")
        message = "もっと話したいんだね:okk:\n"
        talk_contents = generate_talk_cont(message_sent)
        message += talk_contents.replace("@", "`@`")
        post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/add"):
        message_sent = message_sent.replace("/add", "")
        message = "私はこんな人なんだね！！ 教えてくれてありがとう！！\n"
        add_system_settings(message_sent)
        post_to_traq(message, body["message"]["channelId"])

    elif message_sent.startswith("/new"):
        message_sent = message_sent.replace("/new", "")
        message = "新しい私になったよ！！ これからよろしくね！！\n"
        new_system_settings(message_sent)
        post_to_traq(message, body["message"]["channelId"])

    elif message_sent == "/del":
        message = "私は何者でもなかったんだね...:sad_blob_cat_girl:\n"
        new_system_settings("")
        post_to_traq(message, body["message"]["channelId"])

    elif message_sent == "/show":
        message = "私の中身はこんな感じだよ！！\n"
        message += "`" + system_settings + "`"
        post_to_traq(message, body["message"]["channelId"])

    elif message_sent.startswith("/personal"):
        message_sent = message_sent.replace("/personal", "")
        user = body["message"]["user"]["name"]
        if message_sent.startswith(" cont"):
            message_sent = message_sent.replace("cont", "")
            message = "もっと話したいんだね:okk:\n"
            talk_contents = generate_talk_cont_personal(
                message_sent, user)
            message += talk_contents.replace("@", "`@`")
            post_to_traq(
                message, body["message"]["channelId"])
            return Response(status_code=204)
        elif message_sent.startswith(" add"):
            message_sent = message_sent.replace("add", "")
            message = "私はこんな人なんだね！！ 教えてくれてありがとう！！\n"
            add_settings_personal(message_sent, user)
            post_to_traq(
                message, body["message"]["channelId"])
        elif message_sent.startswith(" new"):
            message_sent = message_sent.replace("new", "")
            message = "新しい私になったよ！！ これからよろしくね！！\n"
            new_settings_personal(message_sent, user)
            post_to_traq(
                message, body["message"]["channelId"])
        elif message_sent == " del":
            message = "私は何者でもなかったんだね...:sad_blob_cat_girl:\n"
            new_settings_personal("", user)
            post_to_traq(
                message, body["message"]["channelId"])
        elif message_sent == " show":
            message = "私の中身はこんな感じだよ！！\n"
            message += "`" + settings_personal(user) + "`"
            post_to_traq(
                message, body["message"]["channelId"])
        else:
            message = body["message"]["user"]["displayName"] + \
                "さん :oisu-1::oisu-2::oisu-3::oisu-4yoko:\n"
            talk_contents = generate_talk_personal(
                message_sent, user)
            message += talk_contents.replace("@", "`@`")
            post_to_traq(
                message, body["message"]["channelId"])

    else:
        message = body["message"]["user"]["displayName"] + \
            "さん :oisu-1::oisu-2::oisu-3::oisu-4yoko:\n"
        talk_contents = generate_talk(message_sent)
        message += talk_contents.replace("@", "`@`")
        post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)


def create_response_message(message_type: str) -> str:
    return get_message_text(message_type)


__all__ = ["message_created_response"]
