# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Data as WeatherData
from .serializers import DataSerializer


class Data(APIView):
    def get(self, request):
        data = WeatherData.objects.all()
        serializer = DataSerializer
        return Response(serializer.data)

    def post(self):
        pass


def index(request):
    return HttpResponse("<h1>This is a good day</h1>")

