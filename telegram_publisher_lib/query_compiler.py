import os
from typing import List

from .models import (
    TelegramRequest,
    TelegramQuery
)


def _get_pair(key, value):
    if key == 'chat_name':
        return f"chat_id={os.getenv(value)}"
    return f"{key}={value}"


def compile_query(query: TelegramQuery):
    if query is None:
        raise ValueError("compile_query must have query passed. it is None.")
    key_value_pairs: List[str] = [_get_pair(key, value)
                                  for key, value in query.dict().items()]
    return "&".join(key_value_pairs)


def get_token(request: TelegramRequest):
    if request.token is None:
        raise Exception("Request token alias (`token`) cannot be null")
    return os.getenv(request.token)
