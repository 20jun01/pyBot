from .functions import open_ai
def generate_image(prompt: str):
    return open_ai.image_generate(prompt)
__all__ = ['generate_image']