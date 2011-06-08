from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from todos.api import TaskResource
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()



urlpatterns = patterns('',
        ('^$', direct_to_template, {'template': 'index.html'}),
        ('^api/', include('api.urls'))
)
