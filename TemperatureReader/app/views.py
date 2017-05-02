# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.template import loader
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data as WeatherData
from .serializers import DataSerializer
from .models import Data
import plotly
from plotly.graph_objs import Scatter, Layout
from django import forms


class AddData(CreateView):
    model = Data
    fields = ['temperature', 'time_read']
    widgets = {'time_read': forms.DateTimeInput}

    def get_success_url(self):
        return reverse('timeseries')


class JSONData(APIView):
    def get(self, request):
        data = WeatherData.objects.all()
        serializer = DataSerializer(data, many=True)
        jsondata = serializer.data
        return Response(jsondata)

    def post(self):
        pass


def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def timeseries(request):
    qs = WeatherData.objects.all()
    df = qs.to_dataframe(fieldnames=['time_read', 'temperature'])
    plotly.offline.plot({
        "data": [Scatter(x=df['time_read'], y=df['temperature'])],
        "layout": Layout(title="Temperature Range in Nairobi")})
    templ = loader.get_template('temp-plot.html')
    return HttpResponse(templ.render())










