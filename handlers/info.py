from api.method import send_message
from utils import filters, message_utils

import json

help_text = 'Prints info about the message.'


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'info')

    if params is not None:
        if not params == [] and params[0] == 'help':
            result = help_text
        else:
            result = '```' + json.dumps(message.json, indent=2) + '```'

        send_message(message.chat.id, result, parse_mode='Markdown')
        return True
