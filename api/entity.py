import json

class File:
	def __init__(self, content, is_binary=False, name=None):
		self.content = content
		self.is_binary = is_binary
		self.name = name


class Update:
	def __init__(self, json_data):
		self.json = json_data
		self.update_id = json_data.get('update_id')
		self.message = Message.from_json(json_data.get('message'))
		self.edited_message = Message.from_json(json_data.get('edited_message'))
		self.channel_post = Message.from_json(json_data.get('channel_post'))
		self.edited_channel_post = Message.from_json(json_data.get('edited_channel_post'))
		# self.inline_query = InlineQuery.from_json(json_data.get('inline_query'))
		# self.chosen_inline_result = ChosenInlineResult.from_json(json_data.get('chosen_inline_result'))
		self.callback_query = CallbackQuery.from_json(json_data.get('callback_query'))
		# self.shipping_query = ShippingQuery.from_json(json_data.get('shipping_query'))
		# self.pre_checkout_query = PreCheckoutQuery.from_json(json_data.get('pre_checkout_query'))

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return Update(json_data)


class Message:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.message_id = json_data.get('message_id')
		self.user = User.from_json(json_data.get('from'))
		self.date = json_data.get('date')
		self.chat = Chat.from_json(json_data.get('chat'))
		self.forward_from = User.from_json(json_data.get('forward_from'))
		self.forward_from_chat = Chat.from_json(json_data.get('forward_from_chat'))
		self.forward_from_message_id = json_data.get('forward_from_message_id')
		self.forward_signature = json_data.get('forward_signature')
		self.forward_date = json_data.get('forward_date')
		self.reply_to_message = Message.from_json(json_data.get('reply_to_message'))
		self.edit_date = json_data.get('edit_date')
		self.author_signature = json_data.get('author_signature')
		self.text = json_data.get('text')
		self.entities = json_data.get('entities')  # todo
		# self.audio = Audio.from_json(json_data.get('audio'))
		# self.document = Document.from_json(json_data.get('document'))
		# self.game = Game.from_json(json_data.get('game'))
		self.photo = json_data.get('photo')
		# self.sticker = Sticker.from_json(json_data.get('sticker'))
		# self.video = Video.from_json(json_data.get('video'))
		# self.voice = Voice.from_json(json_data.get('voice'))
		# self.video_note = VideoNote.from_json(json_data.get('video_note'))
		self.caption = json_data.get('caption')
		# self.contact = Contact.from_json(json_data.get('contact'))
		# self.location = Location.from_json(json_data.get('location'))
		# self.venue = Venue.from_json(json_data.get('venue'))
		self.new_chat_member = User.from_json(json_data.get('new_chat_member'))
		self.left_chat_member = User.from_json(json_data.get('left_chat_member'))
		self.new_chat_title = json_data.get('new_chat_title')
		self.new_chat_photo = json_data.get('new_chat_photo')
		self.delete_chat_photo = json_data.get('delete_chat_photo')
		self.group_chat_created = json_data.get('group_chat_created')
		self.supergroup_chat_created = json_data.get('supergroup_chat_created')
		self.channel_chat_created = json_data.get('channel_chat_created')
		self.migrate_to_chat_id = json_data.get('migrate_to_chat_id')
		self.migrate_from_chat_id = json_data.get('migrate_from_chat_id')
		self.pinned_message = Message.from_json(json_data.get('pinned_message'))
		# self.invoice = Invoice.from_json(json_data.get('invoice'))
		# self.successful_payment = SuccessfulPayment.from_json(json_data.get('successful_payment'))
		self.connected_website = json_data.get('connected_website')

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return Message(json_data)


class Chat:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.id = json_data.get('id')
		self.type = json_data.get('type')
		self.title = json_data.get('title')
		self.username = json_data.get('username')
		self.first_name = json_data.get('first_name')
		self.last_name = json_data.get('last_name')
		self.all_members_are_administrators = json_data.get('all_members_are_administrators')
		# self.photo = ChatPhoto.from_json(json_data.get('photo'))
		self.description = json_data.get('description')
		self.invite_link = json_data.get('invite_link')
		self.pinned_message = Message.from_json(json_data.get('pinned_message'))
		self.sticker_set_name = json_data.get('sticker_set_name')
		self.can_set_sticker_set = json_data.get('can_set_sticker_set')

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return Chat(json_data)


class User:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.id = json_data.get('id')
		self.is_bot = json_data.get('is_bot')
		self.first_name = json_data.get('first_name')
		self.last_name = json_data.get('last_name')
		self.username = json_data.get('username')
		self.language_code = json_data.get('language_code')

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return User(json_data)


class InlineKeyboardMarkup:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.inline_keyboard = json_data.get('inline_keyboard')

	def __init__(self, inline_keyboard):
		self.inline_keyboard = inline_keyboard

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return InlineKeyboardMarkup(json_data)


class InlineKeyboardButton:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.text = json_data.get('text')
		self.url = json_data.get('url')
		self.callback_data = json_data.get('callback_data')
		self.switch_inline_query = json_data.get('switch_inline_query')
		self.switch_inline_query_current_chat = json_data.get('switch_inline_query_current_chat')
		# self.callback_game = CallbackGame.from_json(json_data.get('callback_game'))
		self.pay = json_data.get('pay')

	def __init__(self,
				 text,
				 url=None,
				 callback_data=None,
				 switch_inline_query=None,
				 switch_inline_query_current_chat=None,
				 callback_game=None,
				 pay=None):
		self.text = text
		self.url = url
		self.callback_data = callback_data
		self.switch_inline_query = switch_inline_query
		self.switch_inline_query_current_chat = switch_inline_query_current_chat
		# self.callback_game = callback_game
		self.pay = pay

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return InlineKeyboardButton(json_data)


class CallbackQuery:
	def __init__(self, json_data):
		if not json_data:
			return
		self.json = json_data
		self.id = json_data.get('id')
		self.user = User.from_json(json_data.get('from'))
		self.message = Message.from_json(json_data.get('message'))
		self.inline_message_id = json_data.get('inline_message_id')
		self.chat_instance = json_data.get('chat_instance')
		self.data = json_data.get('data')
		self.game_short_name = json_data.get('game_short_name')

	@staticmethod
	def from_json(json_data):
		if not json_data:
			return None
		return CallbackQuery(json_data)
