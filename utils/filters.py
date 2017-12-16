from config import BOT_NAME

import re


def command(text, command_name, split=True, separator=' ', cut_command=True):
    command_name = '/' + command_name
    pattern = '^' + command_name + '(\\s|$)'

    if text == command_name:
        return []
    if re.search(pattern, text):
        if cut_command:
            text = re.sub(pattern, '', text).strip()
        if not split or separator == '':
            return [text]
        return text.split(separator)
    else:
        return None


def name(text, separators={', '}):
    if text.startswith(BOT_NAME):
        if separators:
            for s in separators:
                if text.startswith(BOT_NAME + s):
                    return True
            return False
        else:
            return True
