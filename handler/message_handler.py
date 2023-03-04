from fastapi import Response
from . import talk_handler, response_handler

def message_created_response(body: dict) -> Response:
    if body["message"]["user"]["bot"]:
            print("message from bot")
            return Response(status_code=204)

    message_sent = body["message"]["plainText"]

    if message_sent.startswith("/cont"):
        message="@" + body["message"]["user"]["name"] + " もっと話したいんだね:okk:\n" + talk_handler.generate_talk_cont(message_sent)
        response_handler.send_message(message, body["message"]["channelId"])
        return Response(status_code=204)

    else:
        message=body["message"]["user"]["displayName"] + "さん :oisu-1::oisu-2::oisu-3::oisu-4yoko:\n" + talk_handler.generate_talk(message_sent)
        response_handler.send_message(message, body["message"]["channelId"])
        return Response(status_code=204)
    