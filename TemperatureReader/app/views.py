# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data as WeatherData
from .serializers import DataSerializer
from .models import Data
import plotly
from plotly.graph_objs import Scatter, Layout


class AddData(CreateView):
    model = Data
    fields = ['temperature', 'time_read']


class JSONData(APIView):
    def get(self, request):
        data = WeatherData.objects.all()
        serializer = DataSerializer(data, many=True)
        jsondata = serializer.data
        return Response(jsondata)

    def post(self):
        pass


def index(request):
    return HttpResponse("<h1>This is a good day</h1>")


def timeseries(request):
    qs = WeatherData.objects.all()
    df = qs.to_dataframe(fieldnames=['time_read', 'temperature'])
    return HttpResponse(plotly.offline.plot({
        "data": [Scatter(x=df['time_read'], y=df['temperature'])],
        "layout": Layout(title="The best graph")}))










