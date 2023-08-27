from dotenv import load_dotenv

load_dotenv()
from models import HealthCheck
import handler
from fastapi import FastAPI, HTTPException, Request, Response, status


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
    event = handler.verification_handler(request.headers)
    return handler.event_handler(event, await request.json())
