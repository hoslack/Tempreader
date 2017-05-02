# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from unittest import *
from views import *
from requests import get, post


class AppViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/app/')
        self.assertEqual(resp.status_code, 200)

    def test_series_returns_path(self):
        self.assertEqual(timeseries(get), 'file:///home/hos/Desktop/Tempreader/TemperatureReader/temp-plot.html')






