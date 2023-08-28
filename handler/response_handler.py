import json
import requests
import os

# constants
BOT_ACCESS_TOKEN = os.environ["BOT_ACCESS_TOKEN"]
TRAQ_API_URL = os.environ["TRAQ_URL"]
BOT_ID = os.environ["BOT_ID"]
BASIC_HEADERS: dict = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"
}

def get_headers_to_traq() -> dict:
    return BASIC_HEADERS

def get_channel_file_ids(channel_id: str) -> list:
    url: str = f"{TRAQ_API_URL}/files"
    query: dict = {
        "channelId": channel_id,
        "limit": 20,
        "offset": 0,
        "order": "desc",
        "mine": False
    }
    r: requests.Response = requests.get(url, params=query, headers=BASIC_HEADERS)
    response_body = r.json()
    return [file["id"] for file in response_body]


def get_file_url(file_id: str) -> str:
    return "https://q.trap.jp/files/" + file_id + "/thumbnail"


def post_file(file_path: str, channel_id: str) -> str:
    url: str = f"{TRAQ_API_URL}/files"
    data = {'channelId': channel_id}
    with open(file_path, 'rb') as f:
        files = {'file': f}
        r: requests.Response = requests.post(url, data=data, files=files, headers={"Authorization": f"Bearer {BOT_ACCESS_TOKEN}"})
        response_body = r.json()
        print(response_body)
        return response_body["id"]


def post_to_traq(text: str, channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/channels/{channel_id}/messages"
    data: dict = {
        "content": text,
        "embed": True
    }
    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=BASIC_HEADERS)
    response_body = r.json()


def join_channel(channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/bots/{BOT_ID}/actions/join"
    data: dict = {
        "channelId": channel_id
    }

    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=BASIC_HEADERS)


def leave_channel(channel_id: str) -> None:
    url: str = f"{TRAQ_API_URL}/bots/{BOT_ID}/actions/leave"
    data: dict = {
        "channelId": channel_id
    }

    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=BASIC_HEADERS)


__all__ = ["post_to_traq", "join_channel", "leave_channel", "post_file"]
