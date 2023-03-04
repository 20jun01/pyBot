import json, requests, os

# 環境変数からaccess tokenを読み込む*1
BOT_ACCESS_TOKEN = os.environ["BOT_ACCESS_TOKEN"]

# textをchannel_idに投稿する関数*3
def post_to_traq(text: str, channel_id: str) -> None:
    url: str = f"https://q.trap.jp/api/v3/channels/{channel_id}/messages"
    data: dict = {
        "content": text,
        "embed": True
    }
    headers: dict = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"  # BOTからのtraQへのリクエストにはaccess tokenが必要*1
    }
    r: requests.Response = requests.post(
        url, data=json.dumps(data), headers=headers)
    response_body = r.json()
    print(response_body)