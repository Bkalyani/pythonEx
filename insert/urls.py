#from django.conf.urls.defaults import patterns, include, url
from django.conf.urls import patterns, url, include
from insert.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import settings

# stuff
urlpatterns = patterns('',
       
        url(r'^$', jquerycbox.as_view()),
        url(r'^saveData$', saveData.as_view()),
        url(r'^deleteData$', deleteData.as_view()),
        url(r'^updateData$', updateData.as_view()),
       
)
