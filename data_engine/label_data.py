from world import *
from labels import *
import csv

# location of files with CSV data
csvdata = ['museums_and_galleries.csv',
           'parks_and_green_spaces.csv',
           'Monuments_in_Parks_and_Green_Spaces.csv',
           'play_areas.csv',
           'community_centres.csv',
           'outdoor_education_providers.csv',
           'sport_and_recreational_facilities.csv',
	   'test_locations.csv']
data_dir = 'datasets/'
csvdata = [ data_dir + filename for filename in csvdata ]
#csvdata = [open(d) for d in csvdata]

texts = ['type', 'description', 'name']
sets = ['activities', 'features', 'age_groups']
bools = ['sport', 'brave', 'travel', 'friendly', 'exploration', 'nature', 'learning']
coordinates = ['location']
defined = texts + sets + bools + coordinates

# returns difference of two sets a \ b
def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

def fill(target, space, default):
    for s in space:
        if s not in target:
		target.update({ s : default })

bools_to_one = lambda field : { b : field for b in bools }

# field map our_field_name : field_name_in_file
# fixed - always set to this value
# default - if no value set to this
# defaults our_field_name : default_value
def process_data(csvfile, fieldmap, fixed={}, default={}, delimiter=',', quotechar='"'):
    # Make sure all defined will be there with proper value
    fill(fieldmap, bools, False)
    fill(default, bools, False)
    fill(default, coordinates, '-3.0, 51.0')
    fill(default, texts, '')
    fill(default, sets, [])
    fieldmap.update({ d : None for d in defined if d not in fieldmap.keys()})    
    #print fieldmap

    csvdict = csv.DictReader(open(csvfile), delimiter=delimiter,  quotechar=quotechar)
    data = []

    for row in csvdict:
        obj = {f : fixed[f] for f in fixed.keys()}
            
        for field in diff(fieldmap, fixed):
            if fieldmap[field] != None:
                #print row, fieldmap[field]
                cell = row[fieldmap[field]]
            else:
                cell = default[field]

            if cell in [None, ''] and field in default:
                value = default[field]
                    
            if field in sets:
                exec ('accepted = ' + field) in globals(), locals()
                value = []
		if isinstance(cell, str):
                    cell = cell.lower()
                for a in accepted:
                    if a in cell:
                        value.append(a)
            elif field in bools:
                exec ('satisfying = ' + field) in globals(), locals()
                value = False
                for s in satisfying:
                    if s in cell:
                        value = True
                        break
            elif field in coordinates:
                if cell == '':
                    print csvfile, row
                x, y = cell.split(',')
                value = Point(x, y)
            else:
                value = cell
            obj.update({ field : value })
	#print obj
        data.append(obj)
    return data
            

def dict2loc(d):    
    return Location(d['location'], d['type'], d['name'], [ ds for ds in bools if d[ds] ], d['features'], d['description'])

def dict2area():
    pass

    
def store_data(data_sets):
    # merge then into kd-tree
    pass

# Extract data
# Museums and galleries
fieldmap = bools_to_one('Details')
fieldmap.update({'name' : 'Name', 'features' : 'Details', 'age_groups' : 'Details', 'location' : 'Location'})
museums = process_data(csvdata[0], fieldmap=fieldmap, fixed={'type' : 'Museum', 'exploration' : True, 'learning' : True, 'outdoor' : False}, default={})

# Parks and green spaces
fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'address' : 'Address', 'features' : 'Facilities', 'age_groups' : 'Facilities', 'location' : 'Location', 'postcode' : 'Postcode', 'telephone': 'Telephone', 'email': 'Email', 'open': 'Opening hours'})
parks = process_data(csvdata[1], fieldmap=fieldmap, fixed={'type' : 'Park', 'nature' : True, 'learning' : True, 'outdoor' : True}, default={})

# Monuments in parks and green spaces
fieldmap = bools_to_one('Monument')
fieldmap.update({'name' : 'Monument', 'area': 'Location', 'features' : 'Information', 'location' : 'Location map', 'age_groups' : 'Information'})
monuments = process_data(csvdata[2], fieldmap=fieldmap, fixed={'type' : 'History', 'travel' : True, 'exploration' : True, 'learning' : True, 'outdoor' : True}, default={})

# Play areas
fieldmap = bools_to_one('Play facilities')
fieldmap.update({'name' : 'Site', 'features' : 'Play facilities', 'activities': 'Play facilities', 'location' : 'Location map', 'age_groups' : 'Play facilities', 'address': 'Address', 'postcode': 'Postcode', 'telephone': 'Telephone'})
play_areas = process_data(csvdata[3], fieldmap=fieldmap, fixed={'type' : 'Play Area', 'sport' : True, 'friendly' : True, 'nature' : 'True', 'outdoor' : True}, default={})

# Community centres
fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'features' : 'Facilities', 'age_groups' : 'Facilities', 'location' : 'Location'})
community_centres = process_data(csvdata[4], fieldmap=fieldmap, fixed={'type' : 'Community Centre', 'friendly' : True, 'learning' : True, 'outdoor' : False}, default={})

# Outdoor education providers
fieldmap = bools_to_one('Activities')
fieldmap.update({'name' : 'Name', 'features' : 'Activities', 'age_groups' : 'Activities', 'location' : 'Location'})
outdoor_educators = process_data(csvdata[5], fieldmap=fieldmap, fixed={'type' : 'Outdoor sport', 'sport' : True, 'learning' : True, 'nature' : True, 'outdoor' : True}, default={})

# Sports and recreationial facilities
fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'features' : 'Facilities', 'age_groups' : 'Facilities', 'location' : 'Location', 
		 'activities' : 'Activities', 'address' : 'Address', 'postcode' : 'Postcode', 'telephone': 'Telephone',
		 'email' : 'Email', 'open': 'Opening hours', 'timetable' : 'Timetables', 'cost' : 'Prices',
		 'url' : 'More information'})
sport_facilities = process_data(csvdata[6], fieldmap=fieldmap, fixed={'type' : 'Indoor sport', 'sport' : True, 'friendly' : True, 'outdoor' : False}, default={})

#fieldmap = bools_to_one('type')
#fieldmap = fieldmap.update({'location' : 'location', 'name' : 'name', 'type' : 'type'})
#test_locations = process_data(csvdata[7], fieldmap=fieldmap, fixed={'friendly' : True}, default={})

r = museums + parks + monuments + play_areas + community_centres + outdoor_educators + sport_facilities #+ test_locations
#print play_areas

print parks

data = map(dict2loc, r)

for x in r:
    p = x['age_groups']
    n = x['name']
    o = x['outdoor']
    a = x['activities']
    f = x['features']
    """
    if len(a) > 0:
	   print n, f, a
	   print "---"
    """

"""
counter = 0
for x in r:
    if isinstance(x['location'], Point) and x['location'].x != 51.0 and x['location'].y != -3.0:
        counter += 1    
    else:
        print x
print counter
"""

"""
counter = 0
for x in r:
    if 'outdoor' not in x:
        counter += 1
        print x
print counter
"""
