from django.conf.urls import patterns, include, url
from tic.views import BoardCreate
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('', 
	url(r'^create/', BoardCreate.as_view(),name='board_create'),  

	url(r'^play/', 'tic.views.play'),  

)

