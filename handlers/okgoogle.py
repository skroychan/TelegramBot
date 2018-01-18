from api.method import send_message
from utils import message_utils
from utils.debug import debug_with_forward

import re, urllib

pattern = '^(ok([ea]y)? google)'


def handler(update):
    message = update.message
    text = message_utils.get_text_or_caption(message)
    if not text:
        return

    if re.search(pattern, text, flags=re.IGNORECASE):
        try:
            text = re.sub(pattern, '', text, flags=re.IGNORECASE)
            if not text:
                if message.reply_to_message:
                    text = message_utils.get_text_or_caption(message.reply_to_message)
                if not text:
                    return
            text = text.strip()
            quote_text = urllib.parse.quote_plus(text, safe='')
            result = '[https://www.google.com/search?q=' + text.replace(' ', '+') + '](https://www.google.com/search?q=' + quote_text + ')'
            send_message(message.chat.id, result, parse_mode='Markdown', disable_web_page_preview=True)
            return True
        except Exception as e:
            debug_with_forward(message, repr(e))
