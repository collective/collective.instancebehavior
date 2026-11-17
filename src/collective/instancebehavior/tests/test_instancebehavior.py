from collective.instancebehavior import disable_behaviors
from collective.instancebehavior import enable_behaviors
from collective.instancebehavior import instance_behaviors_of
from collective.instancebehavior.interfaces import IInstanceBehaviorAssignableContent
from collective.instancebehavior.tests import InstanceBehavior_FUNCTIONAL_TESTING
from collective.instancebehavior.tests import ITestBehavior
from plone.behavior.interfaces import IBehaviorAssignable
from plone.dexterity.utils import createContentInContainer
from zope.interface import alsoProvides

import unittest

BEHAVIOR = "collective.instancebehavior.test"


class TestInstanceBehavior(unittest.TestCase):
    layer = InstanceBehavior_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.item = createContentInContainer(
            self.portal, "TestItem", id="item", checkConstraints=False
        )
        alsoProvides(self.item, IInstanceBehaviorAssignableContent)

    def supports_behavior(self, obj):
        return IBehaviorAssignable(obj).supports(ITestBehavior)

    def catalogued_providing_behavior(self):
        brains = self.portal.portal_catalog.unrestrictedSearchResults(
            object_provides=ITestBehavior.__identifier__
        )
        return [brain.getId for brain in brains]

    def test_no_instance_behaviors(self):
        self.assertEqual(instance_behaviors_of(self.item), ())
        self.assertFalse(self.supports_behavior(self.item))

    def test_enable_behaviors(self):
        enable_behaviors(self.item, [BEHAVIOR], [ITestBehavior])
        self.assertEqual(instance_behaviors_of(self.item), [BEHAVIOR])
        self.assertTrue(ITestBehavior.providedBy(self.item))
        self.assertTrue(self.supports_behavior(self.item))
        self.assertEqual(self.catalogued_providing_behavior(), ["item"])

    def test_enable_behaviors_twice(self):
        enable_behaviors(self.item, [BEHAVIOR], [ITestBehavior])
        enable_behaviors(self.item, [BEHAVIOR], [ITestBehavior])
        self.assertEqual(instance_behaviors_of(self.item), [BEHAVIOR])

    def test_disable_behaviors(self):
        enable_behaviors(self.item, [BEHAVIOR], [ITestBehavior])
        disable_behaviors(self.item, [BEHAVIOR], [ITestBehavior])
        self.assertEqual(instance_behaviors_of(self.item), [])
        self.assertFalse(ITestBehavior.providedBy(self.item))
        self.assertTrue(IInstanceBehaviorAssignableContent.providedBy(self.item))
        self.assertFalse(self.supports_behavior(self.item))
        self.assertEqual(self.catalogued_providing_behavior(), [])

    def test_content_without_assignable_marker(self):
        other = createContentInContainer(
            self.portal, "TestItem", id="other", checkConstraints=False
        )
        enable_behaviors(other, [BEHAVIOR], [ITestBehavior])
        self.assertEqual(instance_behaviors_of(other), [BEHAVIOR])
        self.assertFalse(self.supports_behavior(other))
