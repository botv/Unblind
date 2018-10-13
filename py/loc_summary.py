# from pprint import pprint


def locational_summary(objects):

    strings = []
    vertex_list = []
    for obj in objects:
        formatted_string = ''
        for vertex in obj.bounding_poly.normalized_vertices:
            vertex_list.append((vertex.x,vertex.y))
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

        x_str = ''
        if center_x > 0.666:
            x_str += ' to your right'
        elif center_x < 0.333:
            x_str += ' to your left'

        y_str = ''

        if center_y < 0.333:
            y_str += ' above you.'
        elif center_y < 0.666:
            y_str += ' directly in front of you.'
        else:
            y_str += ' below you.'

        # if y_str == '':
        formatted_string += 'There is a ' + obj.name + x_str + y_str
        # else:
        #     formatted_string += 'There is a ' + obj.name + x_str + ' and ' + y_str

        strings.append(formatted_string)

    print(strings)
    return strings

