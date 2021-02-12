import json

import pytest

from telegram_publisher_lib.models import TelegramRequest, TelegramMessageQuery
from telegram_publisher_lib.telegram_client import post_message


def test_successful_telegram_request_model():
    message = {
        "token": "TEST_TOKEN",
        "method": "message",
        "query": TelegramMessageQuery(
            chat_name="chat_id",
            text="String"
        ),
    }
    TelegramRequest(**message)


def test_failing_telegram_request_model_whenWrongMethodPassed():
    message = {
        "token": "TEST_TOKEN",
        "method": "nonEnumMessage",
        "query": TelegramMessageQuery(
            chat_name="chat_name",
            text="String"
        ),
    }
    with pytest.raises(ValueError):
        TelegramRequest(**message)


def test_message_not_sent_when_wrong_token_passed():
    request = TelegramRequest(**{
        "token": "WRONG_TOKEN",
        "method": "message",
        "query": {
            "chat_name": "test_chat",
            "text": "String"
        }
    })
    content = post_message(request)
    assert content.status_code == 404


# def test_sends_message():
#     events = {
#         "token": "test_telegram_token",
#         "method": "message",
#         "query": {
#             "chat_name": "test_chat",
#             "text": "String"
#         }
#     }
#     assert handler(events=events, context="context")['status_code'] == 200
