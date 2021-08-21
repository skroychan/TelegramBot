from api.method import send_message
from utils import filters, message_utils

import random

value_error_text = 'Arguments must be positive integers.'
dice_error_text = 'Use "XdX" syntax to roll dice.\n' \
                  '*Example:* `/rand 2d20`'
dice_big_error_text = 'Your dice are too big 😳'
help_text = 'No arguments: *random number* from 1 to 9.\n1 argument: from 1 to argument.\n' \
            '2 arguments: from 1st argument to 2nd.\n' \
			'*Example:* `/rand 1 10`'

max_song_id = 9999900


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

        elif params[0] == '.i.':
            result = '8'
            for _ in range(random.randint(3, 49)):
                result += '='
            result += 'э'

        elif params[0] == 'song':
            result = 'https://music.yandex.ru/track/' + str(random.randint(1, max_song_id))

        elif len(params) == 1:
            try:
                if 'd' in params[0]:
                    try:
                        dice = params[0].split('d', 1)
                        if int(dice[0]) * (len(dice[1]) + 5) > 4000:
                            result = dice_big_error_text
                        else:
                            result = ''
                            sum = 0
                            for i in range(int(dice[0])):
                                num = random.randint(1, int(dice[1]))
                                result += str(num) + ' + '
                                sum += num
                            result = result[:-2] + '= ' + str(sum)
                    except ValueError:
                        result = dice_error_text
                else:
                    result = random.randint(1, int(params[0]))
            except ValueError:
                result = value_error_text

        elif len(params) == 2:
            try:
                result = random.randint(int(params[0]), int(params[1]))
            except ValueError:
                result = value_error_text
                
        if not result and result != 0:
            return False
        
        send_message(message.chat.id, result, parse_mode='Markdown')
        return True
