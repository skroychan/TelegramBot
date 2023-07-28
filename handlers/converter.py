from api.method import send_message
from utils import message_utils

from operator import itemgetter
import re, json
import urllib.request


supported_currencies = [ 
	"AUD", "AZN", "GBP", "AMD", "BYN", "BGN", "BRL", "HUF", "VND", "HKD", "GEL", "DKK", "AED", "USD", "EUR", "EGP",
	"INR", "IDR", "KZT", "CAD", "QAR", "KGS", "CNY", "MDL", "NZD", "NOK", "PLN", "RON", "XDR", "SGD", "TJS", "THB",
	"TRY", "TMT", "UZS", "UAH", "CZK", "SEK", "CHF", "RSD", "ZAR", "KRW", "JPY"
]

value_pattern = '(\d+(?:\.\d+)?)'
multiplier_pattern = '([KКkк]*)'

max_multiplier = 5


def handler(update):
	message = update.message
	text = message_utils.get_text_or_caption(message)
	if not text:
		return False

	currency_patterns = build_patterns()

	currency_values = match_currencies(text.lower(), currency_patterns)
	if not currency_values:
		return False

	conversion_info = get_conversion_info(currency_values)

	target_currency = get_chat_target_currency(message.chat.id)
	result_lines = build_result_lines(conversion_info, target_currency)
	if not result_lines:
		return False

	result = '\n'.join(result_lines)
	send_message(message.chat.id, result, parse_mode='Markdown')
	return True


def build_patterns():
	patterns = []
	for currency_code in supported_currencies:
		currency_match_info = currencies_match_dict.get(currency_code)

		postfix_pattern = currency_code
		if currency_match_info:
			if currency_match_info.postfix_regex:
				postfix_pattern += '|' + currency_match_info.postfix_regex
			if currency_match_info.sign_regex:
				postfix_pattern += '|' + currency_match_info.sign_regex
		pattern = '(?:' + value_pattern + ' *' + multiplier_pattern + ' *(?:' + postfix_pattern +'))(?:$|\s|[,.:!*;\/\)\(])'

		if currency_match_info and currency_match_info.sign_regex:
			pattern = '(?:' + currency_match_info.sign_regex + value_pattern + ' *' + multiplier_pattern + '|' + pattern + ')'

		patterns.append((currency_code, pattern))

	return patterns


def match_currencies(text, currency_patterns):
	matches = []
	for currency_code, pattern in currency_patterns:
		for match in re.finditer(pattern, text, flags=re.IGNORECASE):
			match_groups = [x for x in match.groups() if x is not None]
			value = float(match_groups[0])
			multiplier = match_groups[1]
			if multiplier and len(multiplier) < max_multiplier:
				value *= 1000 ** len(multiplier)
			matches.append((match.start(), CurrencyValue(currency_code, value)))

	matches.sort(key = itemgetter(0))
	return [itemgetter(1)(x) for x in matches]


def get_conversion_info(currency_values):
	conversion_info = []
	info = json.load(urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')).get("Valute")
	for currency_value in currency_values:
		currency_info = info.get(currency_value.currency_code)
		nominal = float(currency_info.get("Nominal"))
		value = float(currency_info.get("Value")) / nominal
		previous_value = float(currency_info.get("Previous")) / nominal
		conversion_info.append(ConversionInfo(currency_value.currency_code, currency_value.value, value, previous_value))

	return conversion_info


def build_result_lines(conversion_info, target_currency):
	lines = []
	for info in conversion_info:
		converted_target_value = info.source_value * info.target_value
		source_string = '{:,}'.format(info.source_value).replace(',', ' ').rstrip('0').rstrip('.') + ' ' + info.currency_code
		converted_string = '{:,}'.format(round(converted_target_value, 2)).replace(',', ' ') + ' ' + target_currency

		change_string = ''
		if info.source_value == 1:
			change = info.target_value - info.previous_target_value
			change_string = ' _(' + ('↓' if change < 0 else '↑') + '{:,}'.format(round(abs(change), 2)).replace(',', ' ') + ')_'

		lines.append(source_string + ' = ' + converted_string + change_string)

	return lines


# todo config
def get_chat_target_currency(chat_id):
	return "RUB"


class CurrencyPatternInfo:
	def __init__(self, sign_regex, postfix_regex):
		self.sign_regex = sign_regex
		self.postfix_regex = postfix_regex

class CurrencyValue:
	def __init__(self, currency_code, value):
		self.currency_code = currency_code
		self.value = value

class ConversionInfo:
	def __init__(self, currency_code, source_value, target_value, previous_target_value):
		self.currency_code = currency_code
		self.source_value = source_value
		self.target_value = target_value
		self.previous_target_value = previous_target_value

currencies_match_dict = {
	'USD': CurrencyPatternInfo('\$', '(?:доллар(?:ов|а)?|ба(?:кс(?:ов|а)?|чей))'),
	'EUR': CurrencyPatternInfo('€', 'евров?'),
	'BGN': CurrencyPatternInfo(None, 'лев(?:ов|а)?'),
	'UAH': CurrencyPatternInfo('₴', 'гр(?:н|ив(?:ень?|н[ыаiя]))'),
	'AMD': CurrencyPatternInfo(None, 'драм(?:ов|а)?'),
	'PLN': CurrencyPatternInfo(None, 'злот(?:ый|ого|ых)'),
	'INR': CurrencyPatternInfo(None, 'руп(?:ия|ии|ий)'),
	'RON': CurrencyPatternInfo(None, 'ле(?:й|я|ев)'),
	'RSD': CurrencyPatternInfo(None, 'динар(?:а|ов)?'),
	'KZT': CurrencyPatternInfo(None, '(?:тенге|тг)'),
	'THB': CurrencyPatternInfo(None, 'бат(?:а|ов)?')
}
