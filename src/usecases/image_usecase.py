from .. import api_adapters


def edit_image_from_url(image_url: str, prompt: str):
    return api_adapters.edit_image_from_url(image_url, prompt)


def generate_image(prompt: str):
    return api_adapters.generate_image(prompt)
