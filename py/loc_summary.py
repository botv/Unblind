from pprint import pprint
def locational_summary(objects):
    vertex_list = []
    for obj in objects:
        for vertex in obj.bounding_poly.normalized_vertices:
            vertex_list.append((vertex.x,vertex.y))
        min_x = min(vertex_list, key = lambda t: t[0])
        max_x = max(vertex_list, key = lambda t: t[0])
        min_y = min(vertex_list, key = lambda t: t[1])
        max_y = max(vertex_list, key = lambda t: t[1])
        pprint('Min_x:'+str(min_x))
        pprint('Max_x:'+str(max_x))
        pprint('Min_y:'+str(min_y))
        pprint('Max_y:'+str(max_y))
