import requests

default_file_name = "image"
inc = 0
def save_image_from_url_without_name(url: str) -> str:
    global inc
    response = requests.get(url)
    image = response.content
    file_name = default_file_name + str(inc) + ".png"
    inc += 1
    with open(file_name, "wb") as f:
        f.write(image)
    return file_name

def save_image_from_url(url: str, file_name: str):
    response = requests.get(url)
    image = response.content
    with open(file_name, "wb") as f:
        f.write(image)

__all__ = ["save_image_from_url", "save_image_from_url_without_name"]