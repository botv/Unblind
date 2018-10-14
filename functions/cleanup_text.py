import json
import os

from autocorrect import spell


def sort_string(texts):
	top_3 = []
	output = {}
	for text_ in texts["blocks"]:
		text = text_["text"]
		char_area = text_["height"] * text_["width"] / len(text_["text"])
		output.update({text: char_area})

	sorted_output = sorted(output, key=output.get, reverse=True)

	count = 0
	while count < 3 | count < len(sorted_output):
		top_3.append(sorted_output[count])
		count = count + 1

	return top_3


def spell_check(top_3):
	new_strs = []
	new_str = ''
	for str in top_3:
		for word in str.split():
			if len(word) == 1 and ord(word[0]) < 65:
				new_str += word + ' '
			else:
				new_str += spell(word) + ' '
		new_strs.append(new_str)
	return new_strs
