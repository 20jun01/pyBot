from .. import usecases

# TODO: Response型にするのはここの責務なのでそのまま返すのではなく変換する
def generate_image(prompt: str):
    return usecases.generate_image(prompt)


def edit_image_from_url(image_url: str, prompt: str):
    return usecases.edit_image_from_url(image_url, prompt)

__all__ = ["generate_image"]