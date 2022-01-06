from api.method import send_message, delete_message
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
            reply_message_id = message.reply_to_message.message_id if message.reply_to_message else None
            if to == message.chat.id:
                delete_message(message.chat.id, message.message_id)
            send_message(to, result, parse_mode="Markdown", reply_to_message_id=reply_message_id)
            return True
