# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_pandas.managers import DataFrameManager


class Data(models.Model):
    temperature = models.DecimalField(decimal_places=2, max_digits=5)
    time_read = models.DateTimeField()
    objects = DataFrameManager()




