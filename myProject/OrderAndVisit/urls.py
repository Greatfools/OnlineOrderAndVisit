from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^search', views.search, name = 'search'),

	url(r'^ligin', views.login, name = 'login'),
	url(r'^personIformation', views.personIformation, name = 'personInformation')
]