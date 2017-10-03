from api.method import send_message
from utils import message_utils

import random

probability = 0.005
max_length = 40  # 0 - no limit


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    if (max_length <= 0 or len(text) <= max_length) and random.random() <= probability:
        text = text[::-1]
        send_message(message.chat.id, text.encode('utf-8'))
        return True
