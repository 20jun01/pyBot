from pydantic import BaseModel

class TalkResponse(BaseModel):
    message: str

class HealthCheck(BaseModel):
    status: str = "OK"

__all__ = ["TalkResponse", "HealthCheck"]