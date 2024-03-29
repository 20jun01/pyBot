import os
from fastapi import HTTPException

verificationToken = os.getenv("VERIFICATION_TOKEN")


# TODO: middleware的に作る
def verification_handler(headers) -> str:
    print(headers)
    try:
        event = headers["X-TRAQ-BOT-EVENT"]
        reqID = headers["X-TRAQ-BOT-REQUEST-ID"]
        token = headers["X-TRAQ-BOT-TOKEN"]
        if event =="PING":
            return event
    except KeyError:
        raise HTTPException(status_code=403, detail="Forbidden")

    if token != verificationToken:
        raise HTTPException(status_code=403, detail="Forbidden")

    return event


__all__ = ["verification_handler"]
