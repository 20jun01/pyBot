from fastapi import FastAPI, HTTPException, Request, Response
from handler import verification_handler, event_handler

app = FastAPI()

@app.get("/")
async def root():
    print("Hello World")
    return {"message": "Hello World"}

@app.post("/")
async def root(request: Request):
    print(request)
    event = verification_handler.verification_handler(request.headers)
    print(event)
    return event_handler.event_handler(event, await request.json())
