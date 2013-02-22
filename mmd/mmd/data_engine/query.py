# example usage at the bottom

from data import tree # kd tree ballanced around location data
from geometry import Infinity, Circle
from labels import types

# some age_groups and features items got mixed, I think it is because of wrong
# mapping set-up in the batch program
# nothing to do with yours part, but just wanted to let know if one result seems
# out of place (mapping is done in label_data.py)

# for result as a dictionary use any_2_dict(_other_method_)
# ex. any_2_dict(get_them_all())
def any_2_dict(x):
    if x in [None, []]:
        return {}
    if isinstance(x[0], tuple):
        return [ data[1].data.__dict__ for data in x ]
    else:
        return [ t.data.__dict__ for t in x ]

# creates output for map
def get_for_map(x, accepted_fields):
    return [ xs for xs in x if xs in accepted_fields ]

# returns dictionary with 3 fields:
# . 'location'    : (longitude, latitude)
# . 'name'        : name
# . 'type'        : type (e.g. Museum, Gallery, Park etc.)
# . 'description' : description
def get_for_map_summary(x):
    accepted_fields = ['location', 'name', 'type', 'description']
    return get_for_map(x, accepted_fields)

def get_them_all():
    return tree.in_area(Infinity())

# centre should be point Point(longitude, latitude) or in easy peasy saying Point(x, y)
def get_in_radius(centre, radius):
    return tree.in_area(Circle(centre, radius))

# user is instance of User, which class is in user.py
def get_them_all_scored(user):
    return user.rate_and_sort(get_them_all())

def get_in_radius_scored(user, centre, radius):
    return user.rate_and_sort(get_in_radius(centre, radius))

def get_top_n(n, user):
    return get_them_all_scored(user)[0:n]

def get_top_n_in_radius(n, user, centre, radius):
    return get_in_radius_scored(user, centre, radius)[0:n]

def get_top_10(user):
    return get_top_n(10, user)

def get_top_10_in_radius(user, centre, radius):
    return get_top_n_in_radius(10, user, centre, radius)

def get_top_3(user):
    return get_top_n(3, user)

def get_top_3_in_radius(user, centre, radius):
    return get_top_n_in_radius(3, user, centre, radius)

def get_top_3_in_radius_2_dict(user, centre, radius):
    return [ t.data.__dict__ for t in get_top_3_in_radius(user, centre, radius) ]

def good_weather(user, centre, radius):
    return any_2_dict([ y for (x, y) in (get_top_10_in_radius(user, centre, radius)) ])

def bad_weather(user, centre, radius):
    locs = [ y.data for (x,y) in get_in_radius_scored(u, Point(51.0, -3.0), 100.0) ]
    indoors = []
    for l in locs:
        if not l.outdoor:
            indoors.append(l)
            if len(indoors) > 9:
                break
    return [ i.__dict__ for i in indoors ]



def count_types(data):
    counts = { t : 0 for t in types }
    for d in data:
        counts[d['type']] += 1
    return counts

def ulli_data(data):
    if data in [None, ""]:
        return ""
    ulli = "<ul>"
    for li in data:
        ulli += "<li>" + li + "</li>"
    ulli += "</ul>"
    return ulli


def get_singleton_connected(all_points):
    connectable = ['Museum', 'History', 'Play Area', 'Park']

    connected  = [ p for p in all_points if p['type'] in connectable ]
    singletons = [ p for p in all_points if p['type'] not in connectable ]
    return [singletons, connected]


def generate_bottom(data):
    print data
    bottom = ""
    for d in data:
        bottom += "<div class='qwery'><h1>" + d['name'] + '(%f, %f)' % (d['x'], d['y']) + "</h1>"
        if 'type' in d:
            bottom += "<h2>Type: " + d['type'] + "</h2>"
        if 'description' in d and d['description']:
            bottom += "<h2>Description:</h2><p>" + d['description'] + "</p>"
        if 'feature' in d.keys():
            bottom += "<h2>Features</h2>"
            bottom += ulli_data(d['feature'])
        if 'activities' in d.keys():
            bottom += "<h2>Activities:</h2>"
            bottom += ulli_data(d['activities'])+"</div>"
    return bottom



def generate_page(data):
    page = """<div id="cm-example" style="width: 900px; height: 700px; float : left"></div>
  <div id="panel" style="width: 200px; height : 500px; float: left; padding-left: 10px"></div>
  <div id="panel2" style="width: 200px; height : 500px; float: left; padding-left: 10px"></div>
  <div id="panel3" style="width: 200px; height : 500px; float: left; padding-left: 10px"></div>
  
  <script language="JavaScript" type="text/javascript" src="http://tile.cloudmade.com/wml/latest/web-maps-lite.js"></script>

  <script type="text/javascript">
    var tuple = """ + str(get_singleton_connected(data).replace('True','true').replace('False','false')) + \
"""    var user_location = [55.3213, -3.21312]; 
    var generalInterestList = tuple[0];
    var top3List = tuple[1];

    var cloudmade = new CM.Tiles.CloudMade.Web({key: 'eb9238c6dc0248efb8cc8d6a285df878'});
    var map = new CM.Map('cm-example', cloudmade);
    map.setCenter(new CM.LatLng(55.945, -3.187), 15);
  
 //Our favourite place
    var infList = new Array();
    infList[0] = {name: "Appleton Tower", coordinates: [55.944436,-3.186819]};

//Routing
    //if (top3List.length >= 3) {
    var directions = new CM.Directions(map, "panel", 'eb9238c6dc0248efb8cc8d6a285df878')
    var waypoints = [new CM.LatLng(user_location[0],user_location[1]), new CM.LatLng(top3List[0].x,top3List[0].y)];
    directions.loadFromWaypoints(waypoints, {
        travelMode : 'foot', 
        preserveViewport : 'true', 
        draggableWaypoints : 'true'
    }); 

    var directions1 = new CM.Directions(map, "panel2", 'eb9238c6dc0248efb8cc8d6a285df878')
    var waypoints1 = [new CM.LatLng(top3List[0].x, top3List[0].y), new CM.LatLng(top3List[1].x,top3List[1].y)];
    directions.loadFromWaypoints(waypoints1, {
        travelMode : 'foot', 
        preserveViewport : 'true', 
        draggableWaypoints : 'true'
    }); 

    var directions2 = new CM.Directions(map, "panel3", 'eb9238c6dc0248efb8cc8d6a285df878')
    var waypoints2 = [new CM.LatLng(top3List[1].x,top3List[1].y), new CM.LatLng(top3List[2].x, top3List[2].y)];
    directions2.loadFromWaypoints(waypoints2, {
        travelMode : 'foot', 
        preserveViewport : 'true', 
        draggableWaypoints : 'true'
    }); 
    //}

//Icons   
    var infIcon = new CM.Icon();
    infIcon.image = "markers/computers.png";
    infIcon.iconSize = new CM.Size(32, 37);
    museumIcon = new CM.Icon(infIcon, "markers/museum.png");
    parksIcon = new CM.Icon(infIcon, "markers/park.png");
    historicalIcon = new CM.Icon(infIcon, "markers/historical.png");
    cemetaryIcon = new CM.Icon(infIcon, "markers/grave.png");
    outdoorEducationIcon = new CM.Icon(infIcon, "markers/outdooreducation.png");
    communityCentreIcon = new CM.Icon(infIcon, "markers/communitycenter.png");
    mobileLibraryIcon = new CM.Icon(infIcon, "markers/library.png");
    playAreasIcon = new CM.Icon(infIcon, "markers/playground.png");
    sportsIcon = new CM.Icon(infIcon, "markers/sports.png");

//alert(generalInterestList[0].x, generalInterestList[0].y);
//alert(generalInterestList.length);
for (var i = 0; i < generalInterestList.length; i++) {
        if (generalInterestList[i].type == 'Museum') 
           display(museumIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'Park') 
           display(parksIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'History') 
           display(historicalIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'cemetary') 
           display(cemetaryIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'Outdoor sport') 
           display(outdoorEducationIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'mobile_library') 
           display(mobileLibraryIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'Play Area') 
           display(playAreasIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'Indoor sport') 
           display(sportsIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else if (generalInterestList[i].type == 'Community centre') 
           display(communityCentreIcon, generalInterestList[i].type, generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
        else display(generalInterestList[i].name, [generalInterestList[i].x, generalInterestList[i].y]);
    }

function display(ic, type, name, location) {
    var myMarkerLatLng = new CM.LatLng(location[0], location[1]);
    var myMarker = new CM.Marker(myMarkerLatLng, {
        title: name,
        icon: ic
    });
    map.addOverlay(myMarker);
}    

function display(name, location) {
    var myMarkerLatLng = new CM.LatLng(location[0], location[1]);
    var myMarker = new CM.Marker(myMarkerLatLng, {
	title: name
    });
    map.addOverlay(myMarker);
}
</script>"""

    html = page + get_bottom(data)
    return html

########


############


# example usage
from user import test_users
from geometry import Point

print "\n\n\n\n\n\n\n\n\n\n"
for u in test_users(1):
    # get bad weather
    bad = bad_weather(u, Point(51.0, -3.0), 1000.0)
    bad_4_map = get_singleton_connected(bad_weather(u, Point(51.0, -3.0), 1000.0))
    print len(bad_4_map[0]) + len(bad_4_map[1])
    print bad_4_map
    print "\n\n---\n\n"
    # get good weather
    good = good_weather(u, Point(51.0, -3.0), 1000.0)
    good_4_map = get_singleton_connected(good_weather(u, Point(51.0, -3.0), 1000.0))
    print len(good_4_map[0]) + len(good_4_map[1])
    print good_4_map
    print "\n\n---\n\n"
    # count types
    print count_types(bad)
    print count_types(good)
    # print bottom for website
    print "\n\n---\n\n"
    print generate_bottom(bad)
    print "\n\n...\n\n"
    print generate_bottom(good)
    #print [ y for (x,y) in get_in_radius_scored(u, Point(51.0, -3.0), 100.0) ]
#    print get_10_to_map(u, Point(51.0, -3.0), 7.5)
    #x= any_2_dict(get_top_10(u))[2]
    #print x['feature']
    """print any_2_dict(get_top_10(u))
    for x in any_2_dict(get_top_10(u)):
        if 'features' in x.keys():
            print x['features']
    """
    #print generate_bottom(any_2_dict(get_top_10(u)))
