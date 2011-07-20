from django.contrib import admin
from data.models import (Ages, LivingAlone, MedianAge, HomeOwner, ThreeGen, 
                         NinetytoHundred, MedianHouseholdSize, FamilyType, 
                         UnmarriedPartners)

class AgesAdmin(admin.ModelAdmin):
    pass

class LivingAloneAdmin(admin.ModelAdmin):
    pass

class MedianAgeAdmin(admin.ModelAdmin):
    pass

class HomeOwnerAdmin(admin.ModelAdmin):
    pass

class ThreeGenAdmin(admin.ModelAdmin):
    pass

class NinetytoHundredAdmin(admin.ModelAdmin):
    pass

class MedianHouseholdSizeAdmin(admin.ModelAdmin):
    pass

class FamilyTypeAdmin(admin.ModelAdmin):
    pass

class UnmarriedPartnersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ages, AgesAdmin)
admin.site.register(LivingAlone, LivingAloneAdmin)
admin.site.register(MedianAge, MedianAgeAdmin)
admin.site.register(HomeOwner, HomeOwnerAdmin)
admin.site.register(ThreeGen, ThreeGenAdmin)
admin.site.register(NinetytoHundred, NinetytoHundredAdmin)
admin.site.register(MedianHouseholdSize, MedianHouseholdSizeAdmin)
admin.site.register(FamilyType, FamilyTypeAdmin)
admin.site.register(UnmarriedPartners, UnmarriedPartnersAdmin)