# -*- coding: utf-8 -*-
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class InstanceBehaviorLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import collective.instancebehavior

        self.loadZCML(package=collective.instancebehavior, context=configurationContext)

    def setUpPloneSite(self, portal):
        pass

    def tearDownZope(self, app):
        pass


InstanceBehavior_FIXTURE = InstanceBehaviorLayer()
InstanceBehavior_INTEGRATION_TESTING = IntegrationTesting(
    bases=(InstanceBehavior_FIXTURE,), name="InstanceBehavior:Integration"
)
