from .functions import open_ai, image_util
import re
import cv2
import numpy as np
import random

default_file_name = "mask"
inc = 0

async def generate_image(prompt: str):
    return await open_ai.image_generate(prompt)

def edit_image(message: str) -> (str, bool):
    file_urls = re.findall(r'https?://q\.trap\.jp/\S+', message)
    if len(file_urls) == 0:
        return "何をすればいいのかな？", False
    prompt = re.sub(r'https?://q\.trap\.jp/\S+', '', message).strip()
    image_path = image_util.save_image_from_url_without_name(file_urls[-1])
    mask_path = generate_mask(image_path)
    return open_ai.image_edit(image_path, mask_path, prompt), True

def generate_mask(image_path: str) -> str:
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

    # 画像のサイズを取得
    height, width, _ = image.shape

    # 画像を4分割する座標を計算
    segments = [
        (0, 0, width // 2, height // 2),
        (width // 2, 0, width, height // 2),
        (0, height // 2, width // 2, height),
        (width // 2, height // 2, width, height)
    ]

    x1, y1, x2, y2 = random.choice(segments)

    # 透過マスクを作成
    mask = np.ones((height, width), dtype=np.uint8) * 255
    mask[y1:y2, x1:x2] = 0

    # 透過マスクを適用して新しい画像を生成
    image[:, :, 3] = mask

    mask_image_path = default_file_name + str(inc) + ".png"

    cv2.imwrite(mask_image_path, image)
    return mask_image_path

__all__ = ['generate_image', 'edit_image']