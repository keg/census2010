import sys, csv
from django.conf import settings
from location.models import County
from data.models import (Ages, HomeOwner, ThreeGen, NinetytoHundred, 
                         MedianHouseholdSize, FamilyType, UnmarriedPartners, 
                         MedianAge, LivingAlone)
try: 
    file_name = sys.argv[1]
    data_model = sys.argv[2]
except:
    print "Need a filename and datamodel"
    sys.exit(2)

file_reader = csv.reader(open('%s/_input/csv/%s' % 
                              (settings.BASEDIR, file_name), 'rb'), 
                         delimiter=',')

for i, row in enumerate(file_reader):
    values = []
    if i == 0:
        fields = row
        continue
    else:
        county = County.objects.get(county_id=row[0])
        for j, value in enumerate(row[2:]):
            value = value.strip('%,')
            if value == '#DIV/0!':
                value = 0
            elif value != '' and value != ' ':
                try: 
                    value = int(value)
                except ValueError:
                    value = float(value)
                values.append((fields[j+2].strip(), value))
    value_dict =  dict(values)
    a = eval(data_model)(geography = county, **value_dict)
    a.save()