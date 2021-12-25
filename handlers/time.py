from api.method import send_message
from utils import filters, message_utils

from datetime import datetime


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'time')
    if params is None:
        params = filters.command(text, 'date')

    if params is not None:
        send_message(message.chat.id, str(datetime.now()) + " UTC")
        return True
