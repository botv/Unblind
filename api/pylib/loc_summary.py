from pprint import pprint


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
		# pprint('Min_x:'+str(min_x))
		# pprint('Max_x:'+str(max_x))
		# pprint('Min_y:'+str(min_y))
		# pprint('Max_y:'+str(max_y))

		center_x = (max_x + min_x) / 2
		center_y = (max_y + min_y) / 2

		# Append objects based on where the center of the objects are located to categories

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
		# print(obj.name)

	# print(len(left), len(right), len(center), len(above), len(below))

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
	# print(final)

	return final


def format_str(objects, location):
	formatted_str = location + ', there is ' + print_quantity(group(objects))

	return formatted_str


# Group objects of the same type together into a dict from the object to frequency
# objects is a list
def group(objects):
	freq_dict = {}
	for obj in objects:
		if obj not in freq_dict.keys():
			freq_dict[obj] = 1
		else:
			freq_dict[obj] += 1
	return freq_dict


# objects is a dict
# Returns a string with the correctly formatted objects
def print_quantity(objects):
	formatted_str = ''
	for k, v in objects.items():
		if v == 1:
			formatted_str += 'a ' + str(k) + ', '
		else:
			formatted_str += str(v) + ' ' + str(k) + ', '
		# print(str(v), str(k))
	return formatted_str
