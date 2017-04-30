from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^rest/$', views.JSONData.as_view()),
    url(r'^add/$', views.AddData.as_view(), name='add-data'),
    url(r'^series/$', views.TimeSeriesView.as_view()),
    url(r'^display/$', views.display, name='display'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
