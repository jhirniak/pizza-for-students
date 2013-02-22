import random
from world import Location
from data import Node

# statics
toddler = 0; junior = 1; teen = 2; student = 3; adult = 4; senior = 5

MEAN_VALUE = 4 # out of 0..9
MAX_VALUE = 9

class User:
    def __init__(self, preferences, age):
        self.profile = {
            'sport'       : MEAN_VALUE,
            'brave'       : MEAN_VALUE,
            'travel'      : MEAN_VALUE,
            'friendly'    : MEAN_VALUE,
            'exploration' : MEAN_VALUE,
            'nature'      : MEAN_VALUE,
            'learning'    : MEAN_VALUE,
            }
        for p in self.profile:
            self.profile[p] = preferences[p]
        self.age = age

    def age(self):
        return self.age

    def rate(self, node):
        if isinstance(node, Node):
            location = node.data
        elif isinstance(node, Location):
            location = node
        else:
            return 0

        if (location.has_age_groups() and location.proper_age(self.age)) or not location.has_age_groups():
            return sum([ self.profile[p] * location.get_rating(p) for p in self.profile ])
        else:
            return 0
        
    # return list of locations 
    def rate_and_sort(self, locations):
        scored = []
        for l in locations:
            scored.append((self.rate(l), l))
        return sorted(scored, key=lambda (x, y) : x)[::-1]

    def println(self):
        print self.profile

def wc(text, word):
    if word not in text:
        return 0
    else:
        return 1 + wc(text[text.index(word) + len(word):], word)

def preferences_from_facebook(source):
    cats = ['sport', 'brave', 'travel', 'friendly', 'exploration', 'nature',   'learning']
    facebook_cats = {
        'sport'       : ['Amateur Sports Team','Athlete','Professional Sports Team','School Sports Team','Spas/Beauty/Personal Care','Sports League','Sports/Recreation/Activities','Vitamins/Supplements'],
        'brave'       : ['Automobiles and Parts','Automotive','Business Person','Cars','Community/Government','Company','Computers/Technology','Consulting/Business Services','Editor','Fictional Character','Insurance Company','Internet/Software','Kitchen/Cooking','Lawyer','Legal/Law','Local Business','Musical Instrument','Musician/Band','Non-Profit Organization','Political Organization','Small Business'],
        'travel'      : ['Airport','Bags/Luggage','Coach','Monarch','Producer','Public Places','Tours/Sightseeing','Transit Stop','Transport/Freight','Transportation','Travel/Leisure'],
        'friendly'    : ['Baby Goods/Kids Goods','Bar','Business Services','Chef','Church/Religious Organization','Club','Comedian','Community Organization','Concert Venue','Entertainer','Event Planning/Event Services','Games/Toys','Government Official','Government Organization','News Personality','Non-Governmental Organization (NGO)','Political Party','Radio Station','Shopping/Retail','Teacher','Wine/Spirits'],
        'exploration' : ['Artist','Camera/Photo','Clothing','Dancer','Drugs','Food/Beverages','Jewelry/Watches','Journalist','Magazine','Media/News/Publishing','Mining/Materials','Movie','Movie Theater','Movies/Music','Music Chart','Music Video','Politician','Studio','TV Channel'],
        'nature'      : ['Chemicals','Farming/Agriculture','Health/Beauty','Landmark','Outdoor Gear/Sporting Goods','Patio/Garden','Pet Services','Pet Supplies'],
        'learning'    : ['Actor/Director', 'Aerospace/Defense','Album','Arts/Entertainment/Nightlife','Attractions/Things to Do','Bank/Financial Institution','Bank/Financial Services','Biotechnology','Book','Book Store','Building Materials','Computers','Concert Tour','Doctor','Education','Electronics','Energy/Utility','Engineering/Construction','Health/Medical/Pharmaceuticals','Health/Medical/Pharmacy','Library','Museum/Art Gallery','Telecommunication']
        }
    cats_count = [ sum([ wc(source, fw) for fw in facebook_cats[c] ]) for c in cats ]
    N = sum(cats_count) // MAX_VALUE
    cats_score = [ cc // N for cc in cats_count ]
    return { cats[i] : cats_score[i] for i in range(len(cats)) }

# testing
# all int values from [0..8], total 9
user_example = { 'age' : student, 'sport' : True, 'brave' : False, 'travel' : 4, 'friendly' : 4, 'exploration' : 4, 'nature' : 4, 'learning' : 4 }
test_users = lambda how_many   : \
             [User( { 'sport'       : random.randint(0,10),
                      'brave'       : random.randint(0,10),
                      'travel'      : random.randint(0,10),
                      'friendly'    : random.randint(0,10),
                      'exploration' : random.randint(0,10),
                      'nature'      : random.randint(0,10),
                      'learning'    : random.randint(0,10) },
                      random.randint(0,6)) \
                  for x in range(how_many) ]

#for t in test_users(20):
#    print t
