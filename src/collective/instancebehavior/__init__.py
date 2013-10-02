from zope.annotation import IAnnotations
from zope.component import (
    queryUtility,
    adapter,
)
from zope.interface import (
    alsoProvides,
    noLongerProvides,
)
from plone.behavior.interfaces import IBehavior
from plone.dexterity.behavior import DexterityBehaviorAssignable
from .interfaces import IInstanceBehaviorAssignableContent


ANNOTATION_KEY = 'collective.instancebehavior.instance_behaviors'


@adapter(IInstanceBehaviorAssignableContent)
class DexterityInstanceBehaviorAssignable(DexterityBehaviorAssignable):
    """Support per instance specification of plone.behavior behaviors.
    """

    def __init__(self, context):
        super(DexterityInstanceBehaviorAssignable, self).__init__(context)
        annotations = IAnnotations(context)
        self.instance_behaviors = annotations.get(ANNOTATION_KEY, ())

    def enumerateBehaviors(self):
        self.behaviors = self.fti.behaviors + self.instance_behaviors
        for name in self.behaviors:
            behavior = queryUtility(IBehavior, name=name)
            if behavior is not None:
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
    :type behaviors: list
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
    instance_behaviors = annotations.get(ANNOTATION_KEY, ())
    instance_behaviors += behaviors
    annotations[ANNOTATION_KEY] = instance_behaviors

    for iface in ifaces:
        alsoProvides(obj, iface)

    if reindex:
        obj.reindexObject(idxs=('object_provides'))


def disable_behaviors(obj, behaviors, ifaces, reindex=True):
    """ Disable behaviors on an object.

    :param obj: The Dexterity content object to disable behaviors on.
    :type obj: object
    :param behaviors: Behaviors to be disabled on the object. This is a list of
                      dotted names of behavior schema interfaces.
    :type behaviors: list
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
    instance_behaviors = filter(lambda x: x not in behaviors,
                                instance_behaviors)
    annotations[ANNOTATION_KEY] = instance_behaviors

    for iface in ifaces:
        noLongerProvides(obj, iface)

    if reindex:
        obj.reindexObject(idxs=('object_provides'))
