import json
import requests
import os

BOT_ACCESS_TOKEN = os.environ["BOT_ACCESS_TOKEN"]
TRAQ_API_URL = os.environ["TRAQ_URL"]
BOT_ID = os.environ["BOT_ID"]


def post_to_traq(text: str, channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/channels/{channel_id}/messages"
    data: dict = {
        "content": text,
        "embed": True
    }
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"
    }
    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=headers)
    response_body = r.json()


def join_channel(channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/bots/{BOT_ID}/actions/join"
    data: dict = {
        "channelId": channel_id
    }

    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"
    }

    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=headers)


def leave_channel(channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/bots/{BOT_ID}/actions/leave"
    data: dict = {
        "channelId": channel_id
    }

    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"
    }

    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=headers)


__all__ = ["post_to_traq", "join_channel", "leave_channel"]
