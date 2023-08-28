import requests
import os

default_file_name = "image"
inc = 0
BOT_ACCESS_TOKEN = os.environ["BOT_ACCESS_TOKEN"]


def save_image_from_url_without_name(url: str) -> str:
    global inc
    response = requests.get(url)
    image = response.content
    file_path = default_file_name + str(inc) + ".png"
    inc = (inc + 1) % 10
    with open(file_path, "wb") as f:
        f.write(image)
    return file_path


def save_image_from_url_without_name_with_login(url: str, query: dict = {"type": "image"}, HEADERS: dict = {
                                                "Content-Type": "application/json",
                                                "Authorization": f"Bearer {BOT_ACCESS_TOKEN}"
                                                }) -> str:
    global inc
    HEADERS["accept"] = "image/png"
    response = requests.get(url, params=query, headers=HEADERS)
    image = response.content
    file_path = default_file_name + str(inc) + ".png"
    inc = (inc + 1) % 10
    with open(file_path, "wb") as f:
        f.write(image)
    return file_path


def save_image_from_url(url: str, file_name: str):
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as f:
        f.write(image)


__all__ = ["save_image_from_url", "save_image_from_url_without_name"]
