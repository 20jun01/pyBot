from fastapi import Response, HTTPException
from message_handler import message_created_response

def event_handler(event: str, body: dict) -> Response:
    if event == "PING":
        return Response(status_code=204)
    elif event == "MESSAGE_CREATED":
        message_created_response(body)
        return Response(status_code=204)
    else:
        return HTTPException(status_code=400, detail="Bad Request")