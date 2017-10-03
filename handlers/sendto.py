from api.method import send_message
from utils import filters, message_utils

help_text = '*Sends* a message.\nUsage: /send to=<chatid> <text>. `to` is optional.'
default_error = 'Invalid syntax. See help: `/send help`'
no_text_error = 'You must specify text to send. See help: `/send help`'


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return
    params = filters.command(text, 'send')

    if params is not None:
        result = ''
        to = message.chat.id

        if params == [] or params[0] == 'help':
            result = help_text

        else:
            for param in params:
                if param.startswith('to='):
                    to = param.split('=')[1]
                else:
                    result += param + ' '

        if result:
            send_message(to, result.encode('utf-8'))
            return True
