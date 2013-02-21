# not integral part of the rest of the code

import csv
#from labels import sports

strip_non_alphas = lambda s : ''.join( x for x in s if x.isalpha() or x == ' ' )    
remove_unwanted = lambda s, unwanted : ' '.join( x for x in s.split(' ') if x not in unwanted )
fit_labels = lambda source, target : [ l for l in source if target.index(l) ]

def extract_labels(csvfile, label, delimiter=',', quotechar='"'):
    labels = set()
    csvdict = csv.DictReader(csvfile, delimiter=delimiter,  quotechar=quotechar)
    for d in csvdict:
        for l in d[label].split('\n'):            
            if l != '':
                l = l.lower()
                l = strip_non_alphas(l)
                l = remove_unwanted(l, ['including'])
                labels.add(l)
    return labels

# csvfile = open('sport_and_recreational_facilities.csv')
# print extract_labels(csvfile, 'Activities')

csvfile = open('datasets/play_areas.csv')
print extract_labels(csvfile, 'Play facilities')
