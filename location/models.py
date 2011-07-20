from django.db import models

class State(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    state_id = models.PositiveIntegerField()
    abbrivation = models.CharField(max_length=2)
    
    def __unicode__(self):
        return self.name
    
class County(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    county_id = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField()
    city_id = models.PositiveIntegerField()
    
    def __unicode__(self):
        return self.name