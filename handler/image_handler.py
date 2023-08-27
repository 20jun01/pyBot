from .functions import open_ai
async def generate_image(prompt: str):
    return await open_ai.image_generate(prompt)
__all__ = ['generate_image']