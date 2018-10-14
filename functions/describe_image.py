import io
import os
import sys

from google.cloud import vision
from google.cloud.vision import types


def locational_summary(objects):
	strings = []
	vertex_list = []
	left = []
	right = []
	center = []
	above = []
	below = []
	for obj in objects:
		for vertex in obj.bounding_poly.normalized_vertices:
			vertex_list.append((vertex.x, vertex.y))
		min_x = min(vertex_list, key=lambda t: t[0])[0]
		max_x = max(vertex_list, key=lambda t: t[0])[0]
		min_y = min(vertex_list, key=lambda t: t[1])[1]
		max_y = max(vertex_list, key=lambda t: t[1])[1]

		center_x = (max_x + min_x) / 2
		center_y = (max_y + min_y) / 2

		if center_x > 0.666:
			right.append(obj.name)
		elif center_x < 0.333:
			left.append(obj.name)
		elif center_y < 0.25:
			above.append(obj.name)
		elif center_y > 0.75:
			below.append(obj.name)
		else:
			center.append(obj.name)
	left_formatted = ''
	center_formatted = ''
	right_formatted = ''
	above_formatted = ''
	below_formatted = ''

	if len(left) != 0:
		left_formatted = format_str(left, 'On your left') + ' . '
	if len(right) != 0:
		right_formatted = format_str(right, 'On your right') + ' . '
	if len(center) != 0:
		center_formatted = format_str(center, 'Directly in front of you') + ' . '
	if len(above) != 0:
		above_formatted = format_str(above, 'Above you') + ' . '
	if len(below) != 0:
		below_formatted = format_str(below, 'Below you') + ' . '

	strings.append(center_formatted + left_formatted + right_formatted + above_formatted + below_formatted)

	final = ''
	for string in strings:
		final += string
	return final


def format_str(objects, location):
	formatted_str = location + ', there is ' + print_quantity(group(objects))

	return formatted_str


def group(objects):
	freq_dict = {}
	for obj in objects:
		if obj not in freq_dict.keys():
			freq_dict[obj] = 1
		else:
			freq_dict[obj] += 1
	return freq_dict


def print_quantity(objects):
	formatted_str = ''
	for k, v in objects.items():
		if v == 1:
			formatted_str += 'a ' + str(k) + ', '
		else:
			formatted_str += str(v) + ' ' + str(k) + ', '
	return formatted_str


def exec_summary(labels):
	image_tags = ""
	string = "This image pertains to"
	counter = 0
	for label in labels:
		if (counter == 0 or counter == 1):
			image_tags = image_tags + " " + label.description + ","
			counter += 1
		elif (counter == 2):
			image_tags = image_tags + " and " + label.description
			counter += 1
		else:
			break
	image_tags = image_tags + "."
	string = string + image_tags
	return string


def localize_objects_uri(uri):
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()

	image = vision.types.Image()
	image.source.image_uri = uri

	objects = client.object_localization(
		image=image).localized_object_annotations
	return locational_summary(objects)


def detect_labels_uri(uri):
	from google.cloud import vision
	client = vision.ImageAnnotatorClient()
	image = vision.types.Image()
	image.source.image_uri = uri

	response = client.label_detection(image=image)
	labels = response.label_annotations
	return exec_summary(labels)


def describe_image(request):
	request_json = request.get_json()
	uri = ''
	if request.args and 'uri' in request.args:
		uri = request.args.get('uri')
	elif request_json and 'uri' in request_json:
		uri = request_json['uri']
	else:
		return ''

	response = ''
	response = response + detect_labels_uri(uri) + ' '
	response = response + localize_objects_uri(uri)
	return response
