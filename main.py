from dotenv import load_dotenv

load_dotenv()
from fastapi import FastAPI, Request, status, APIRouter
import src.handler
from src.models import HealthCheck, ImageGenerateRequest, ImageEditRequest


app = FastAPI()


@app.get(
    "/",
    tags=["healthcheck"],
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 204 (No Content)",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=HealthCheck,
)
async def get_health() -> HealthCheck:
    return None


@app.post("/")
async def root(request: Request):
    event = src.handler.verification_handler(request.headers)
    return await src.handler.event_handler(event, await request.json())


open_ai_router = APIRouter(
    prefix="/openai",
    tags=["openai"],
)

open_ai_image_router = APIRouter(
    prefix="/image",
)

# TODO: routerをhandlerに渡して定義を移す(そうするとrequestの型を知る責務がなくなる)


@open_ai_image_router.post("/gen")
async def openai_image_gen(request: ImageGenerateRequest):
    return await src.handler.generate_image(request.prompt)


@open_ai_image_router.post("/edit")
async def openai_image_edit(request: ImageEditRequest):
    return src.handler.edit_image_from_url(request.image_url, request.prompt)


open_ai_router.include_router(open_ai_image_router)
app.include_router(open_ai_router)
