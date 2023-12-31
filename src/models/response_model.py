from pydantic import BaseModel


class TalkResponse(BaseModel):
    message: str


class HealthCheck(BaseModel):
    status: str


__all__ = ["TalkResponse", "HealthCheck"]
