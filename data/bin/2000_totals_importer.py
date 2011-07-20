import sys, csv
from django.conf import settings
from location.models import County
from data.models import (Ages, NinetytoHundred,)

MODELS = (Ages, NinetytoHundred)

try: 
    file_name = sys.argv[1]
except:
    print "Need a filename"
    sys.exit(2)

file_reader = csv.reader(open('%s/_input/csv/%s' % 
                              (settings.BASEDIR, file_name), 'rb'), 
                         delimiter=',')
for model in MODELS:
    for i, row in enumerate(file_reader):
            county = County.objects.get(county_id=row[0])
            a = model.objects.get(geography = county)
            if row[1] != '':
                a.total_population_2000 = row[1] 
            else:
                a.total_population_2000 = 0
            a.save()