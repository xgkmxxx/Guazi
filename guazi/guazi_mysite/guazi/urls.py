from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.list_guazi, name='list_guazi'),
	url(r'^$', views.search, name='search'),
]