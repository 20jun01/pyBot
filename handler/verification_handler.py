import os

verificationToken = os.getenv("VERIFICATION_TOKEN")
def verification_handler(headers) -> bool:
    try:
        event = headers["X-TRAQ-BOT-EVENT"]
        reqID = headers["X-TRAQ-BOT-REQUEST-ID"]
        token = headers["X-TRAQ-BOT-TOKEN"]
    except KeyError:
        return False

    if token != verificationToken:
        return False
    
    return True