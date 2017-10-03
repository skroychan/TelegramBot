from api.method import send_message
from utils import filters, message_utils

import random

value_error_text = 'Arguments must be positive integers.'
help_text = 'No arguments: *random number* from 1 to 9.\n1 argument: from 1 to argument.\n' \
            '2 arguments: from 1st argument to 2nd.'


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'rand')

    if params is not None:
        result = None
        if params == []:
            result = random.randint(1, 9)

        elif params[0] == 'help':
            result = help_text

        elif len(params) == 1:
            try:
                result = random.randint(1, int(params[0]))
            except ValueError:
                result = value_error_text

        elif len(params) == 2:
            try:
                result = random.randint(int(params[0]), int(params[1]))
            except ValueError:
                result = value_error_text
                
        if result:
            send_message(message.chat.id, result, parse_mode='Markdown')
            return True
