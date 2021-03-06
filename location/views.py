from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import RequestContext, Context, loader
from location.models import County
from data.models import (Ages, LivingAlone, MedianAge, HomeOwner, ThreeGen, 
                         NinetytoHundred, MedianHouseholdSize, FamilyType, 
                         UnmarriedPartners)

def profile_detail(request, slug):
    location = get_object_or_404(County, slug__exact=slug)
    ages = Ages.objects.get(geography=location)
    living_alone = LivingAlone.objects.get(geography=location)
    median_age = MedianAge.objects.get(geography=location)
    home_owner = HomeOwner.objects.get(geography=location)
    three_gen = ThreeGen.objects.get(geography=location)
    ninety_to_hundred = NinetytoHundred.objects.get(geography=location)
    median_household_size = MedianHouseholdSize.objects.get(geography=location)
    family_type = FamilyType.objects.get(geography=location)
    unmarried_partners = UnmarriedPartners.objects.get(geography=location)
    
    population_change = ages.total_population_2010 - ages.total_population_2000
    
    t = loader.get_template('profile/base.html')
    c = RequestContext(request, {
        'location': location,
        'ages': ages.__dict__,
        'living_alone': living_alone,
        'median_age': median_age,
        'home_owner': home_owner,
        'three_gen': three_gen,
        'ninety_to_hundred': ninety_to_hundred,
        'median_household_size': median_household_size,
        'family_type': family_type,
        'unmarried_partners': unmarried_partners,
        'population_change': population_change 
    })
    return HttpResponse(t.render(c))

def map_index(request):

    data = {}
    # Get the locations, then get the data
    locations = County.objects.all()
    
    for location in locations:
        ages = Ages.objects.get(geography=location)
        living_alone = Ages.objects.get(geography=location)
        median_age = MedianAge.objects.get(geography=location)
        home_owner = HomeOwner.objects.get(geography=location)
        three_gen = ThreeGen.objects.get(geography=location)
        ninety_to_hundred = NinetytoHundred.objects.get(geography=location)
        median_household_size = MedianHouseholdSize.objects.get(geography=location)
        family_type = FamilyType.objects.get(geography=location)
        unmarried_partners = UnmarriedPartners.objects.get(geography=location)
        
        # Add the values to the data list.        
        data[location.name] = {
            'location': location,
            'ages': ages, 
            #'living_alone': living_alone,
            'median_age': median_age,
            'home_owner': home_owner,
            'three_gen': three_gen,
            'ninety_to_hundred': ninety_to_hundred,
            'median_household_size': median_household_size,
            'family_type': family_type,
            'unmarried_partners': unmarried_partners } 
        #data[location.name] = ages
        data[location.name] = {
            #'location': location,
            'ages': ages, 
            #'living_alone': living_alone,
            'median_age': median_age,
            'home_owner': home_owner,
            'three_gen': three_gen,
            'ninety_to_hundred': ninety_to_hundred,
            'median_household_size': median_household_size,
            'family_type': family_type,
            'unmarried_partners': unmarried_partners } 

    t = loader.get_template('map/index.html')
    c = RequestContext(request, { 'data': data })
    return HttpResponse(t.render(c))