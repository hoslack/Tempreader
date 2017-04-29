# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Data as WeatherData
from .serializers import DataSerializer
from rest_pandas import PandasView, PandasScatterSerializer
from matplotlib import style
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pylab as pl
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


class Data(APIView):
    def get(self, request):
        data = WeatherData.objects.all()
        serializer = DataSerializer(data, many=True)
        jsondata = serializer.data
        return Response(jsondata)

    def post(self):
        pass


class TimeSeriesView(PandasView):
    queryset = WeatherData.objects.all()
    serializer_class = DataSerializer


def index(request):
    return HttpResponse("<h1>This is a good day</h1>")


def display(self):
    pass











