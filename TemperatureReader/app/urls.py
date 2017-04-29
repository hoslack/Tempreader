from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^data/$', views.Data.as_view()),
    url(r'^display/$', views.display, name='display'),
]