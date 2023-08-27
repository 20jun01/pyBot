import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def completion(new_message_text: str, settings_text: str = '', past_messages: list = []):
    """
    This function generates a response message using OpenAI's GPT-3 model by taking in a new message text, 
    optional settings text and a list of past messages as inputs.

    Args:
    new_message_text (str): The new message text which the model will use to generate a response message.
    settings_text (str, optional): The optional settings text that will be added as a system message to the past_messages list. Defaults to ''.
    past_messages (list, optional): The optional list of past messages that the model will use to generate a response message. Defaults to [].

    Returns:
    tuple: A tuple containing the response message text and the updated list of past messages after appending the new and response messages.
    """
    if len(past_messages) == 0 and len(settings_text) != 0:
        system = {"role": "system", "content": settings_text}
        past_messages.append(system)
    new_message = {"role": "user", "content": new_message_text}
    past_messages.append(new_message)

    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=past_messages
    )
    response_message = {"role": "assistant",
                        "content": result.choices[0].message.content}
    past_messages.append(response_message)
    response_message_text = result.choices[0].message.content
    return response_message_text, past_messages


def image_edit(image_path: str, prompt: str = '', size: str = "1024x1024") -> str:
    """
    This function generates an edited image using OpenAI's DALL-E model by taking in an image and an optional prompt as inputs.

    Args:
    image (str): The image that will be edited by the model.
    prompt (str, optional): The optional prompt that will be used by the model to edit the image. Defaults to ''.
    size (str, optional): The optional size of the edited image. Defaults to "1024x1024".

    Returns:
    str: The edited image url.
    """
    image = openai.Image.create_edit(
        image=open(image_path, "rb"),
        prompt=prompt,
        size=size
    )

    return image["data"][0]["url"]


def image_generate(prompt: str = '', size: str = "256x256") -> str:
    """
    Args:
    prompt (str, optional): The optional prompt that will be used by the model to generate the image. Defaults to ''.
    size (str, optional): The optional size of the generated image. Defaults to "1024x1024".

    Returns:
    str: The generated image url.
    """
    image = openai.Image.create(
        prompt=prompt,
        size=size
    )

    return image["data"][0]["url"]

__all__ = ["completion"]
