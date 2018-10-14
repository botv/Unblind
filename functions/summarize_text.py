import json
import os

from autocorrect import spell


def sort_string(blocks):
	top_3 = []
	output = {}
	for text_ in blocks:
		text = text_["text"]
		char_area = text_["height"] * text_["width"] / len(text_["text"])
		output.update({text: char_area})
	sorted_output = sorted(output, key=output.get, reverse=True)
	count = 0
	while count < 3 | count < len(sorted_output):
		top_3.append(sorted_output[count])
		count = count + 1
	return top_3


def check_one_sentence(sentence):
	new_str = ''
	for word in sentence.split():
		if len(word) == 1 and ord(word[0]) < 65:
			new_str += word + ' '
		else:
			new_str += spell(word) + ' '
	return new_str


def spell_check(top_3):
	new_strs = []
	new_str = ''
	for sentence in top_3:
		new_str = check_one_sentence(sentence)
		new_strs.append(new_str)

	return new_strs


def summarize_text(request):
	request_json = request.get_json()
	blocks = []
	if request.args and 'blocks' in request.args:
		blocks = request.args.get('blocks')
	elif request_json and 'blocks' in request_json:
		blocks = request_json['blocks']
	else:
		return ''

	top_3 = sort_string(blocks)
	checked_strings = spell_check(top_3)

	response = ''

	for string in checked_strings:
		response += string + '. '
	return response
