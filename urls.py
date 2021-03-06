from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^census2010/', include('census2010.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),

    #county view
    (r'^census/2010/colorado/county/(?P<slug>[\w-]+)/$', 'location.views.profile_detail'),
)
# 

if settings.DEBUG :
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 
         'django.views.static.serve', 
         {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )