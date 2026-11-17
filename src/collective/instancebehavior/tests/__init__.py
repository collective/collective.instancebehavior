from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.dexterity.fti import DexterityFTI
from zope.interface import Interface


class ITestBehavior(Interface):
    """Behavior the tests enable per instance (its own marker)."""


class InstanceBehaviorLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.instancebehavior
        import collective.instancebehavior.tests

        self.loadZCML(package=collective.instancebehavior, context=configurationContext)
        self.loadZCML(
            "testing.zcml",
            package=collective.instancebehavior.tests,
            context=configurationContext,
        )

    def setUpPloneSite(self, portal):
        fti = DexterityFTI("TestItem")
        fti.klass = "plone.dexterity.content.Item"
        portal.portal_types._setObject("TestItem", fti)


InstanceBehavior_FIXTURE = InstanceBehaviorLayer()
# enable_behaviors and disable_behaviors commit the transaction: each test
# needs its own database.
InstanceBehavior_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(InstanceBehavior_FIXTURE,), name="InstanceBehavior:Functional"
)
