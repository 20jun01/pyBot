from fastapi import FastAPI, HTTPException, Request, Response, status
from handler import verification_handler, event_handler
from models import HealthCheck
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return HealthCheck(status="OK")

@app.post("/")
async def root(request: Request):
    event = verification_handler(request.headers)
    return event_handler(event, await request.json())
