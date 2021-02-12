from enum import Enum

from pydantic import BaseModel, validator


class TelegramMethodEnum(Enum):
    message = "message"


class TelegramQuery(BaseModel):
    chat_name: str


class TelegramMessageQuery(TelegramQuery):
    text: str


class TelegramRequest(BaseModel):
    token: str
    method: TelegramMethodEnum
    query: TelegramMessageQuery

    @validator('method')
    def is_allowed_method(cls, v):
        try:
            TelegramMethodEnum(v)
        except ValueError as e:
            raise e
        return v
