from fastapi import Response, HTTPException
from ..usecases.message_usecase import message_created_response
from ..usecases.stamp_usecase import message_stamp_updated_response


async def event_handler(event: str, body: dict) -> Response:
    if event == "PING":
        return Response(status_code=204)
    elif event == "MESSAGE_CREATED":
        await message_created_response(body)
        return Response(status_code=204)
    elif event == "BOT_MESSAGE_STAMPS_UPDATED":
        await message_stamp_updated_response(body)
        return Response(status_code=204)
    else:
        return HTTPException(status_code=400, detail="Bad Request")


__all__ = ["event_handler"]
