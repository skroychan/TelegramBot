from response import send_response


def send_message(chat_id, text, parse_mode=None, disable_web_page_preview=None, disable_notification=None,
                 reply_to_message_id=None, reply_markup=None):
    if chat_id and text:
        data = {'chat_id': chat_id, 'text': str(text)}
        if parse_mode:
            data['parse_mode'] = parse_mode
        if disable_web_page_preview:
            data['disable_web_page_preview'] = disable_web_page_preview
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        send_response('sendMessage', data)


def send_photo(chat_id, photo, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
    if chat_id and photo:
        data = {'chat_id': chat_id, 'photo': photo}
        if caption:
            data['caption'] = caption
        if disable_notification:
            data['disable_notification'] = disable_notification
        if reply_to_message_id:
            data['reply_to_message_id'] = reply_to_message_id
        if reply_markup:
            data['reply_markup'] = reply_markup
        send_response('sendPhoto', data)


def forward_message(chat_id, from_chat_id, message_id, disable_notification=None):
    if chat_id and from_chat_id and message_id:
        data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
        if disable_notification:
            data['disable_notification'] = disable_notification
        send_response('forwardMessage', data)
