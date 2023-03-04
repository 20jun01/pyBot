from fastapi import FastAPI, HTTPException, Request, Response
from handler import verification_handler, event_handler

app = FastAPI()

@app.post("/")
async def root(request: Request):
    event = verification_handler.verification_handler(request.headers)
    return event_handler.event_handler(event, await request.json())
