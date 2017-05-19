# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from unittest import *
from views import *
from requests import get, post
from models import Data
import datetime


class AppViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/app/')
        self.assertEqual(resp.status_code, 200)

    def test_series_returns_path(self):
        self.assertEqual(timeseries(get), 'file:///home/hos/Desktop/Tempreader/TemperatureReader/temp-plot.html')

    def test_data_instance(self):
        reading = Data()
        self.assertIsInstance(reading, Data, msg='The object should be an instance of the `Data` class')

    def test_datetime_type(self):
        reading = Data()
        self.assertIsInstance(reading.time_read, datetime, msg='The datetime data should be of type datetime')





