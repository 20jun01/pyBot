from .functions import open_ai, image_util
from PIL import Image, ImageDraw
import numpy as np
import random
from .response_handler import get_channel_file_ids, get_file_url

default_file_name = "mask"
inc = 0

async def generate_image(prompt: str):
    return await open_ai.image_generate(prompt)

def edit_image(message: str, channel_id: str) -> (str, bool):
    file_ids = get_channel_file_ids(channel_id)
    prompt = message.replace("[添付ファイル]", "")

    if len(file_ids) == 0:
        return "何をすればいいのかな？", False

    file_url = get_file_url(file_ids[0])
    print(file_url)
    image_path_in_function = image_util.save_image_from_url_without_name(file_url)
    print(image_path_in_function)
    mask_path = generate_mask(image_path_in_function)
    return open_ai.image_edit(image_path_in_function, mask_path, prompt), True

def generate_mask(image_path_in_function: str) -> str:
    # 画像を読み込む
    image = Image.open(image_path_in_function)
    if image is None:
        return "これなに？"

    # 画像のサイズを取得
    width, height = image.size

    # 画像を4分割する座標を計算
    segments = [
        (0, 0, width // 2, height // 2),
        (width // 2, 0, width, height // 2),
        (0, height // 2, width // 2, height),
        (width // 2, height // 2, width, height)
    ]

    x1, y1, x2, y2 = random.choice(segments)

    # 透過マスクを作成
    mask = Image.new('L', (width, height), 255)
    draw = ImageDraw.Draw(mask)
    draw.rectangle([x1, y1, x2, y2], fill=0)

    # 透過マスクを適用して新しい画像を生成
    image.putalpha(mask)

    mask_image_path = default_file_name + str(inc) + ".png"
    inc = (inc + 1) % 10

    image.save(mask_image_path)
    return mask_image_path

import os

def find_file(start_directory, target_file_name):
    for root, dirs, files in os.walk(start_directory):
        if target_file_name in files:
            return os.path.join(root, target_file_name)
    return None

__all__ = ['generate_image', 'edit_image']