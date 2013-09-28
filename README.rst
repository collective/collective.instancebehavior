collective.instancebehavior
===========================

References
----------

http://opkode.net/media/blog/plone-and-dexterity-enable-behaviors-per-content-type-instance
https://gist.github.com/thet/3990769


Problem and Motivation
----------------------

Behaviors, provided by the ``plone.behavior`` package, provide a very useful
way of extending the functionality of a Dexterity content type. Unfortunately,
the fact that a content type's behaviors are stored in its factory contents
information (FTI) inside the portal_types tool, means that they are class
(or type) specific, and not instance specific. This means that behaviors can
only be enabled globally, in other words only for all the instances of a
specific type.

To enable per instance behaviors, we need a way to store those behaviors
on the instance. We use annotations for this purpose.

Additionally We provide our own ``IBehaviorAssignable`` adapter that overrides
the default one to not only look for an object's FTI registered annotations,
but also look for the behaviors stored in the current instance's annotations.

Also helper functions are implemented which can be used to dynamically assing
behaviors and interfaces on dexterity content objects.


Installation
------------

Depend your plone product on ``collective.instancebehavior``.


Enable behaviors and interfaces
-------------------------------

::
    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> enable_behaviors(obj, ['plone.app.event.dx.behaviors.IEventBasic',],
    ...                       [IDXEvent,])


Disable behaviors and interfaces
--------------------------------

::
    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> disable_behaviors(obj, ['plone.app.event.dx.behaviors.IEventBasic',],
    ...                        [IDXEvent,])


Contributors
------------

- JC Brand
- Johannes Raggam
- Robert Niederreiter
