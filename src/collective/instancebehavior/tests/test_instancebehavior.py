import unittest2 as unittest
from collective.instancebehavior.tests import \
    InstanceBehavior_INTEGRATION_TESTING


class TestInstanceBehavior(unittest.TestCase):
    layer = InstanceBehavior_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_foo(self):
        self.assertEquals(1, 1)
