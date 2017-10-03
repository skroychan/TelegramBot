from api.entity import Message


def get_text(message):
    if message and isinstance(message, Message):
        return message.text


def get_text_or_caption(message):
    if message and isinstance(message, Message):
        return message.text or message.caption
