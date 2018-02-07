from response import send_response

import json, urllib


def jsonify(obj):
	return json.dumps(obj, default=lambda o: {k: v for k, v in o.__dict__.items() if v})


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
			data['reply_markup'] = jsonify(reply_markup)
		send_response('sendMessage', data)


def forward_message(chat_id, from_chat_id, message_id, disable_notification=None):
	if chat_id and from_chat_id and message_id:
		data = {'chat_id': chat_id, 'from_chat_id': from_chat_id, 'message_id': message_id}
		if disable_notification:
			data['disable_notification'] = disable_notification
		send_response('forwardMessage', data)


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
			data['reply_markup'] = jsonify(reply_markup)
		send_response('sendPhoto', data)


def send_document(chat_id, document, caption=None, disable_notification=None, reply_to_message_id=None, reply_markup=None):
	if chat_id and document:
		data = {'chat_id': chat_id, 'document': document}
		if caption:
			data['caption'] = caption
		if disable_notification:
			data['disable_notification'] = disable_notification
		if reply_to_message_id:
			data['reply_to_message_id'] = reply_to_message_id
		if reply_markup:
			data['reply_markup'] = jsonify(reply_markup)
		send_response('sendDocument', data)


def delete_message(chat_id, message_id):
	if chat_id and message_id:
		data = {'chat_id': chat_id, 'message_id': message_id}
		send_response('deleteMessage', data)


def answer_callback_query(callback_query_id, text=None, show_alert=None, url=None, cache_time=None):
	if callback_query_id:
		data = {'callback_query_id': callback_query_id}
		if text:
			data['text'] = text
		if show_alert:
			data['show_alert'] = show_alert
		if url:
			data['url'] = url
		if cache_time:
			data['cache_time'] = cache_time
		send_response('answerCallbackQuery', data)


def edit_message_reply_markup(chat_id=None, message_id=None, inline_message_id=None, reply_markup=None):
	data = {}
	if chat_id:
		data['chat_id'] = chat_id
	if message_id:
		data['message_id'] = message_id
	if inline_message_id:
		data['inline_message_id'] = inline_message_id
	if reply_markup:
		data['reply_markup'] = jsonify(reply_markup)
	send_response('editMessageReplyMarkup', data)
