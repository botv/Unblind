"""
Handles text detection including spell check and choosing the top three most important blocks.

Letao Chen, Wesley Tian

10/14/2018

"""


import json
import os

from autocorrect import spell


def sort_string(texts):
    """
    Takes in a JSON file containing like:
    {
        "blocks": [
            {
                "text": "Hello",
                "width": 20,
                "height": 10
            }
        ]
    }

    Returns the top three blocks based on area per character.

    """
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
    """
    Takes in a list of the three strings.
    Runs spell check and returns a list containing the string spellchecked.
    
    Each word is spell checked individually, and non alphanumeric characters that are one letter long are ignored.
    (e.g. &) This is because the AV Speech can read out the ampersands, for example.

    """
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
