# -*- coding: utf-8 -*-
from collective.instancebehavior.tests import (
    InstanceBehavior_INTEGRATION_TESTING,
)

import unittest


class TestInstanceBehavior(unittest.TestCase):
    layer = InstanceBehavior_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]

    def test_foo(self):
        self.assertEqual(1, 1)
