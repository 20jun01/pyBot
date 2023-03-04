from pydantic import BaseModel

class TalkResponse(BaseModel):
    message: str
