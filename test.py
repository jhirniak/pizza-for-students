indoors = [{'y': 33, 'x': 52, 'name': 'test'}, {'y': 33, 'x': 52, 'name': 'test'}, {'y': 33, 'x': 52, 'name': 'test'}, {'y': 33, 'x': 52, 'name': 'test'}, {'y': 33, 'x': 52, 'name': 'test'}]
stringify = lambda i: """infList[""" + str(i) """] = {name: """ + indoors[i]['name'] + """, coordinates: [""" + str(indoors[i]['x']) + """,""" + str(indoors[i]['y']) + """]};"""
print [  stringify(i) for i in range(len(indoors)) ]
