import os

verificationToken = os.getenv("VERIFICATION_TOKEN")
def verificatioN_handler(headers: dict(str)) -> bool:
    try:
        event = headers["X-TRAQ-BOT-EVENT"]
        reqID = headers["X-TRAQ-BOT-REQUEST-ID"]
        token = headers["X-TRAQ-BOT-TOKEN"]
    except KeyError:
        return False

    if token != verificationToken:
        return False
    
    return True