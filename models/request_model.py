from pydantic import BaseModel

class TalkRequest(BaseModel):
    message: str

class ImageGenerateRequest(BaseModel):
    prompt: str

class ImageEditRequest(BaseModel):
    prompt: str
    image_url: str

__all__ = ["TalkRequest", "ImageGenerateRequest", "ImageEditRequest"]