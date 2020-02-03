# -*- coding: utf-8 -*-
from collective.instancebehavior.interfaces import (
    IInstanceBehaviorAssignableContent,
)
from plone.behavior.interfaces import IBehavior
from plone.dexterity.behavior import DexterityBehaviorAssignable
from plone.dexterity.schema import SchemaInvalidatedEvent
from zope.annotation import IAnnotations
from zope.component import adapter
from zope.component import queryUtility
from zope.event import notify
from zope.interface import alsoProvides
from zope.interface import noLongerProvides

import six


ANNOTATION_KEY = "collective.instancebehavior.instance_behaviors"


@adapter(IInstanceBehaviorAssignableContent)
class DexterityInstanceBehaviorAssignable(DexterityBehaviorAssignable):
    """Support per instance specification of plone.behavior behaviors.
    """

    def __init__(self, context):
        super(DexterityInstanceBehaviorAssignable, self).__init__(context)
        annotations = IAnnotations(context)
        self.instance_behaviors = annotations.get(ANNOTATION_KEY, ())

    def enumerateBehaviors(self):
        for behavior in super(
            DexterityInstanceBehaviorAssignable, self
        ).enumerateBehaviors():
            yield behavior
        for name in tuple(self.instance_behaviors):
            behavior = queryUtility(IBehavior, name=name)
            if behavior:
                yield behavior


def instance_behaviors_of(obj):
    """Return applied instance behavior names of object.

    :param obj: The Dexterity content object to enable behaviors on.
    :type obj: object
    """
    annotations = IAnnotations(obj)
    return annotations.get(ANNOTATION_KEY, ())


def enable_behaviors(obj, behaviors, ifaces, reindex=True):
    """Enable behaviors on an object.

    :param obj: The Dexterity content object to enable behaviors on.
    :type obj: object
    :param behaviors: Behaviors to be enabled on the object. This is a list of
                      dotted names of behavior schema interfaces.
    :type behaviors: list or tuple
    :param ifaces: Behavior marker interfaces belonging to the behaviors to be
                   enabled. This is a list of interface classes.
    :type ifaces: class
    :param reindex: Flag whether to reindex object after modification
    :type reindex: bool

    Use it like so:

    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> enable_behaviors(obj, ['plone.app.event.dx.behaviors.IEventBasic',],
    ...                       [IDXEvent,])
    """
    annotations = IAnnotations(obj)
    instance_behaviors = list(annotations.get(ANNOTATION_KEY, []))
    for behavior in behaviors:
        if behavior not in instance_behaviors:
            instance_behaviors.append(behavior)
    annotations[ANNOTATION_KEY] = instance_behaviors

    for iface in ifaces:
        alsoProvides(obj, iface)

    # invalidate global schema cache
    notify(SchemaInvalidatedEvent(portal_type=None))

    if reindex:
        obj.reindexObject(idxs=("object_provides"))


def disable_behaviors(obj, behaviors, ifaces, reindex=True):
    """ Disable behaviors on an object.

    :param obj: The Dexterity content object to disable behaviors on.
    :type obj: object
    :param behaviors: Behaviors to be disabled on the object. This is a list of
                      dotted names of behavior schema interfaces.
    :type behaviors: list or tuple
    :param ifaces: Behavior marker interfaces belonging to the behaviors to be
                   disabled. This is a list of interface classes.
    :type ifaces: class
    :param reindex: Flag whether to reindex object after modification
    :type reindex: bool

    Use it like so:

    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> disable_behaviors(obj, ['plone.app.event.dx.behaviors.IEventBasic',],
    ...                        [IDXEvent,])
    """
    annotations = IAnnotations(obj)
    instance_behaviors = annotations.get(ANNOTATION_KEY, ())
    instance_behaviors = filter(lambda x: x not in behaviors, instance_behaviors)
    if six.PY3:
        instance_behaviors = list(instance_behaviors)
    annotations[ANNOTATION_KEY] = instance_behaviors

    for iface in ifaces:
        noLongerProvides(obj, iface)

    # invalidate global schema cache
    notify(SchemaInvalidatedEvent(portal_type=None))

    if reindex:
        obj.reindexObject(idxs=("object_provides"))
