from fastapi import Response
from . import talk_handler, response_handler


def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
        print("message from bot")
        return Response(status_code=204)

    message_sent = body["message"]["plainText"]

    if message_sent.startswith("/help"):
        message = create_response_message("help")
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("@BOT_urturn_Talker /join"):
        response_handler.join_channel(body["message"]["channelId"])
        message = create_response_message("join")
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/leave"):
        response_handler.leave_channel(body["message"]["channelId"])
        message = create_response_message("leave")
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/cont"):
        message_sent = message_sent.replace("/cont", "")
        message = "@" + body["message"]["user"]["name"] + \
            " もっと話したいんだね:okk:\n"
        talk_contents = talk_handler.generate_talk_cont(message_sent)
        message += talk_contents.replace("@", "`@`")
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)
    
    elif message_sent.startswith("/add"):
        message_sent = message_sent.replace("/add", "")
        message = "@" + body["message"]["user"]["name"] + \
            " 私はこんな人なんだね！！ 教えてくれてありがとう！！\n"
        talk_handler.add_system_settings(message_sent)
        response_handler.post_to_traq(message, body["message"]["channelId"])

    elif message_sent.startswith("/new"):
        message_sent = message_sent.replace("/new", "")
        message = "@" + body["message"]["user"]["name"] + \
            " 新しい私になったよ！！ これからよろしくね！！\n"
        talk_handler.new_system_settings(message_sent)
        response_handler.post_to_traq(message, body["message"]["channelId"])

    elif message_sent == "/del":
        message = "@" + body["message"]["user"]["name"] + \
            " 私は何者でもなかったんだね...:sad_blob_cat_girl:\n"
        talk_handler.new_system_settings("")
        response_handler.post_to_traq(message, body["message"]["channelId"])

    else:
        message = body["message"]["user"]["displayName"] + \
            "さん :oisu-1::oisu-2::oisu-3::oisu-4yoko:\n"
        talk_contents = talk_handler.generate_talk(message_sent)
        message += talk_contents.replace("@", "`@`")
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)


def create_response_message(message_type: str) -> str:
    message = ""
    if message_type == "help":
        message += "## BOT_urturn_Talker\n"
        message += "### どうしたいか教えてね\n"
        message += "#### `/help`: このメッセージを表示するよ\n(/helpから始まればなんでもいいのは内緒ね)\n"
        message += "#### `/cont + {message}`: 前の続きを話そうか\n"
        message += "#### `/join`: 君と話しを始めたいって思えるよ\n"
        message += "#### `/leave`: そんなこと言わないでよ...\n"
        message += "#### `/add + {setting}`: キャラの設定を追加するよ\n"
        message += "#### `/new + {setting}`: キャラの設定を新しくするよ\n"
        message += "#### `/del`: 私の人格を消すよ...\n"
        message += "#### `{message}`: いっぱいお話ししたいな\n"
    elif message_type == "leave":
        message += ":snailchan_jito.ex-large.ex-large:"
    elif message_type == "join":
        message += ":oisu-1::oisu-2::oisu-3::oisu-4yoko:"
    return message
