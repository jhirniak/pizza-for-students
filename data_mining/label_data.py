from location import *
from labels import *
import csv

# location of files with CSV data
csvdata = ['museums_and_galleries.csv',
           'parks_and_green_spaces.csv',
           'Monuments_in_Parks_and_Green_Spaces.csv',
           'play_areas.csv',
           'community_centres.csv',
           'outdoor_education_providers.csv',
           'sport_and_recreational_facilities.csv']
data_dir = 'datasets/'
csvdata = [ data_dir + filename for filename in csvdata ]
#csvdata = [open(d) for d in csvdata]

names = ['type', 'description', 'name']
sets = ['activities', 'features']
bools = ['sport', 'brave', 'travel', 'friendly', 'exploration', 'nature', 'learning']
coordinates = ['location']
defined = names + sets + bools + coordinates

def diff(a, b):
        b = set(b)
        return [aa for aa in a if aa not in b]

# field map our_field_name : field_name_in_file
# defaults our_field_name : default_value
# fixed - always set to this value
# default - if no value set to this
def process_data(csvfile, fieldmap, fixed={}, default={}, delimiter=',', quotechar='"'):
    # Make sure all defined will be there with proper value
    for d in defined:
        if d not in fieldmap:
            if d in bools:
                fixed.update({d : False})
            elif d in coordinates:
                fixed.update({d : Point(51.0,-3.0)})
            else:
                fixed.update({d : ''})
            continue

        if d not in default:
            if d in bools:
                default.update({d : False})
            elif d in coordinates:
                default.update({d : Point(51.0,-3.0)})
            else:
                default.update({d : ''})

        
    print fieldmap

    fieldmap.update({ d : None for d in defined if d not in fieldmap.keys()})
    print fieldmap

    csvdict = csv.DictReader(open(csvfile), delimiter=delimiter,  quotechar=quotechar)
    data = []

    for row in csvdict:
        obj = {}
        
        obj.update(fixed)
            
        for field in diff(fieldmap, fixed):
            if fieldmap[field] != None:
                cell = row[fieldmap[field]]
            else:
                cell = default[field]

            if cell in [None, ''] and field in default:
                value = default[field]
                    
            if field in sets:
                exec ('accepted = ' + field) in globals(), locals()
                value = []
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
                x, y = cell.split(',')
                value = Point(x, y)
            else:
                value = cell
            obj.update({ field : value })
        data.append(obj)
    return data
            

def dict2loc(d):
    print d
    print [ ds for ds in bools ]
    return Location(d['location'], d['type'], d['name'], [ ds for ds in bools if d[ds] ], d['features'], d['description'])

def dict2area():
    pass

    
def store_data(data_sets):
    # merge then into kd-tree
    pass

bools_to_one = lambda field : { b : field for b in bools }
#print bools_to_one('test')


#l1 = Location('Pub', Point(55.1, -3.1), ['outdoor', 'educational'], ['sledge', 'slide'], 'Great for children')
#l2 = Location('Park', Point(55.1, -3.1))
# print l1.name, l1.latitude(), l1.longitude()

fieldmap = bools_to_one('Details')
fieldmap.update({'name' : 'Name', 'features' : 'Details'})
museums = process_data(csvdata[0], fieldmap=fieldmap, fixed={'type' : 'Museum', 'exploration' : True, 'learning' : True}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'address' : 'Address', 'features' : 'Facilities'})
parks = process_data(csvdata[1], fieldmap=fieldmap, fixed={'type' : 'Park', 'nature' : True, 'learning' : True}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Information')
fieldmap.update({'name' : 'Monument', 'area': 'Location', 'features' : 'Information', 'location' : 'Location map'})
monuments = process_data(csvdata[2], fieldmap=fieldmap, fixed={'type' : 'History', 'travel' : True, 'exploration' : True, 'learning' : True}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Play facilities')
fieldmap.update({'name' : 'Site', 'features' : 'Play facilities', 'location' : 'Location map'})
play_areas = process_data(csvdata[3], fieldmap=fieldmap, fixed={'type' : 'Play Area', 'sport' : True, 'friendly' : True, 'nature' : 'True'}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'features' : 'Facilities'})
community_centres = process_data(csvdata[4], fieldmap=fieldmap, fixed={'type' : 'Community Centre', 'friendly' : True, 'learning' : True}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Activities')
fieldmap.update({'name' : 'Name', 'features' : 'Activities'})
outdoor_educators = process_data(csvdata[5], fieldmap=fieldmap, fixed={'type' : 'Outdoor sport', 'sport' : True, 'learning' : True, 'nature' : True}, default={'location' : '51.0, -3.0'})

fieldmap = bools_to_one('Facilities')
fieldmap.update({'name' : 'Name', 'features' : 'Facilities'})
sport_facilities = process_data(csvdata[6], fieldmap=fieldmap, fixed={'type' : 'Indoor sport', 'sport' : True, 'friendly' : True}, default={'location' : '51.0, -3.0'})

r = museums + parks + monuments + play_areas + community_centres + outdoor_educators + sport_facilities

data = map(dict2loc, r)

# for x in data:
#   print x.rating
