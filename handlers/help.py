from api.method import send_message
from utils import filters, message_utils

help_text = 'Available commands:\n/rand - random number\n/send - send a message\n' \
            'Use `/<command> help` for additional info. '


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'help')

    if params is not None:
        send_message(message.chat.id, help_text, parse_mode='Markdown')
        return True
