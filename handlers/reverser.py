from api.method import send_message
from utils import filters, message_utils
from utils.debug import debug_with_forward

import random, re

probability = 0.005
max_length = 40  # 0 - no limit
reverse_parentheses = True  # e.g. (hello) => (olleh) instead of )olleh(
# todo: map


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'reverse', split=False)
    if params is not None and len(params) == 1:
        text = params[0]

    if params is not None or ((max_length <= 0 or len(text) <= max_length) and random.random() <= probability):
        if reverse_parentheses:
            text = re.sub('\((.*)\)', ')\g<1>(', text)
        text = text[::-1]
        try:
            send_message(message.chat.id, text.encode('utf-8'))
            return True
        except UnicodeDecodeError as e:
            debug_with_forward(message, 'Exception: ' + repr(e))
