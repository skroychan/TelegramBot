from api.method import delete_message


def handler(update):
    message = update.message
    if message.new_chat_title or message.new_chat_photo or message.pinned_message:
        delete_message(message.chat.id, message.message_id)
