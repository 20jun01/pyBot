from pydantic import BaseModel

class TalkRequest(BaseModel):
    message: str

class ImageGenerateRequest(BaseModel):
    prompt: str

__all__ = ["TalkRequest", "ImageGenerateRequest"]