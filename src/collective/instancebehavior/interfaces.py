# -*- coding: utf-8 -*-
from plone.dexterity.interfaces import IDexterityContent


class IInstanceBehaviorAssignableContent(IDexterityContent):
    """Marks dexterity content to be extensible by instance behaviors.
    """
