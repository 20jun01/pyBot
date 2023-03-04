from fastapi import FastAPI, HTTPException, Request, Response
from handler import talk_handler, verification_handler
from models.request_model import TalkRequest
from models.response_model import TalkResponse

with open("system_setting.txt", "r") as f:
    system_settings = f.read()

app = FastAPI()


@app.get("/")
async def root(request: Request):
    if verification_handler.verification_handler(request.headers):
        return Response(status_code=204)
    else:
        return HTTPException(status_code=403, detail="Forbidden")


@app.post("/talk", response_model=TalkResponse)
async def generate_talk(request: TalkRequest):
    global past_messages
    new_message, past_messages = talk_handler.talk_handler(
        [], request.message, system_settings)
    return TalkResponse(message=":@BOT_urturn225: < " + new_message)


@app.post("/talk/cont", response_model=TalkResponse)
async def generate_talk(request: TalkRequest):
    global past_messages
    new_message, messages = talk_handler.talk_handler(
        past_messages, request.message, system_settings)
    return TalkResponse(message=":@BOT_urturn225: < " + new_message)
