from fastapi import Response
from . import talk_handler, response_handler

def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
            print("message from bot")
            return Response(status_code=204)

    message_sent = body["message"]["plainText"]

    if message_sent.startswith("/help"):
        message = ""
        message += "コマンド一覧\n"
        message += "/help: このメッセージを表示します\n"
        message += "/cont: トークを続けます\n"
        message += "/join: チャンネルに参加します\n"
        message += "/leave: チャンネルから退出します\n"
        message += "その他: お話しします\n"
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("@BOT_urturn_Talker /join"):
        response_handler.join_channel(body["message"]["channelId"])
        response_handler.post_to_traq(":oisu-1::oisu-2::oisu-3::oisu-4yoko:", body["message"]["channelId"])
        return Response(status_code=204)

    elif message_sent.startswith("/leave"):
        response_handler.leave_channel(body["message"]["channelId"])
        response_handler.post_to_traq(":snailchan_jito.ex-large.ex-large:", body["message"]["channelId"])
        return Response(status_code=204)

    if message_sent.startswith("/cont"):
        message="@" + body["message"]["user"]["name"] + " もっと話したいんだね:okk:\n" + talk_handler.generate_talk_cont(message_sent)
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)

    else:
        message=body["message"]["user"]["displayName"] + "さん :oisu-1::oisu-2::oisu-3::oisu-4yoko:\n" + talk_handler.generate_talk(message_sent)
        response_handler.post_to_traq(message, body["message"]["channelId"])
        return Response(status_code=204)
    