from api.method import send_message, forward_message
from config import ADMIN_ID


def debug(text):
    send_message(ADMIN_ID, text, parse_mode='Markdown')


def debug_with_forward(message, text):
    debug(text)
    forward_message(ADMIN_ID, message.chat.id, message.message_id)
