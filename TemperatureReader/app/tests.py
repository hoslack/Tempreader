# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase


class AppViewsTestCase(TestCase):
    def test_index(self):
        resp = self.client.get('/app/')
        self.assertEqual(resp.status_code, 200)


