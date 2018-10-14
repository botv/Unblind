import json
import os

#modify json objects

#the filename should be modified 
filename = 'block_sample.json'

output = {}

with open(filename, 'r') as f:
    texts = json.load(f)
    for text_ in texts["blocks"]:
        text = text_["text"]
        char_area = text_["height"] * text_["width"] / len(text_["text"])
        output.update( {text : char_area} )

    sorted_output = sorted(output, key=output.get, reverse=True)

    count = 0; 
    while count < 3 | count < len(sorted_output):
    	print(sorted_output[count])
    	count = count + 1