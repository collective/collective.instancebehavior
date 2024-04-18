collective.instancebehavior
===========================

Problem and Motivation
----------------------

Behaviors, provided by the ``plone.behavior`` package, provide a very useful way of extending the functionality of a Dexterity content type.
Unfortunately, the fact that a content type's behaviors are stored in its factory contents information (FTI) inside the portal_types tool, means that they are class (or type) specific, and not instance specific.
This means that behaviors can only be enabled globally, in other words only for all the instances of a specific type.

To enable per instance behaviors, we need a way to store those behaviors on the instance.
We use annotations for this purpose.

Additionally, we provide our own ``IBehaviorAssignable`` adapter that overrides the default one.
It does not only look for an object's FTI registered annotations, but also look for the behaviors stored in the current instance's annotations.

Also helper functions are implemented which can be used to dynamically assing behaviors and interfaces on dexterity content objects.


Installation
------------

Depend your plone addon on ``collective.instancebehavior``.


Enable behaviors and interfaces
-------------------------------

Note: the targeted object must implement ``collective.instancebehavior.IInstanceBehaviorAssignableContent``.

::

    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> enable_behaviors(
    ...     obj,
    ...     ['plone.app.event.dx.behaviors.IEventBasic'],
    ...     [IDXEvent]
    ... )


Disable behaviors and interfaces
--------------------------------

::

    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> disable_behaviors(
    ...     obj,
    ...     ['plone.app.event.dx.behaviors.IEventBasic'],
    ...     IDXEvent]
    ... )


Caching
-------

In some cases (ex: tests), you may need to clear Dexterity assignable cache after enabling or disabling instance behaviors.

::

    >>> from plone.dexterity.content import ASSIGNABLE_CACHE_KEY
    >>> delattr(request, ASSIGNABLE_CACHE_KEY)



Ideas
=====

References
----------

- ``http://opkode.net/media/blog/plone-and-dexterity-enable-behaviors-per-content-type-instance``
- ``https://gist.github.com/thet/3990769``


Support
=======

We appreciate any contribution and if a release is needed to be done on pypi, please just contact one of the contributors.
Some of us also offer commercial support if any training, coaching, integration or adaptions are needed.

If you are having issues, please let us know.

Source Code
-----------

The sources are in a GIT DVCS with its main branches at `github <http://github.com/collective/collective.instancebehavior>`_.
There you can report issue too.

We'd be happy to see many forks and pull-requests to make this addon even better.

This package uses the `black code style <https://github.com/ambv/black/>`_.


Contributors
------------

- JC Brand
- Johannes Raggam
- Robert Niederreiter
- Peter Holzer
- Jens Klein


License
=======

The project is licensed under the GPLv2.
