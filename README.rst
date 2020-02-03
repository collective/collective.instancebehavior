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
    ...     ['plone.app.event.dx.behaviors.IEventBasic',],
    ...     [IDXEvent,]
    ... )


Disable behaviors and interfaces
--------------------------------

::

    >>> from plone.app.event.dx.interfaces import IDXEvent
    >>> disable_behaviors(
    ...     obj,
    ...     ['plone.app.event.dx.behaviors.IEventBasic',],
    ...     IDXEvent,]
    ... )



Ideas
=====

References
----------

- ``http://opkode.net/media/blog/plone-and-dexterity-enable-behaviors-per-content-type-instance``
- ``https://gist.github.com/thet/3990769``


from IRC
--------

::

    12:13 < rnix> datakurre: https://github.com/bluedynamics/bda.plone.productshop/blob/master/bda/plone/productshop/browser/forms.py
    12:13 < rnix> datakurre: woring instance behavior enabled add form
    12:21 < rnix> datakurre: may be generalized to collective.instancebehavior -> just need a generic way on telling DX to use the correct form. -> idea would be to have a
                  behavior which can be bound to folderish objects and this defined default behaviors applied dynamically
    12:21 < rnix> to it's direct children
    12:22 < rnix> but i do not really like to register this add view for every type.. would be more appropriate if we found a way on
    12:22 < rnix> deciding by applied container interface
    12:22 < rnix> something like that...
    12:26 < datakurre> rnix: What the differences for original add form? 1) show fields for default instance behaviors 2) enable default instance behaviors on save?
    12:28 < datakurre> rnix: 2) Could probably be done by instancebehavior-adapter (add form would call it, when instancebehavior-behavior is enabled)
    12:28 < datakurre> rnix: 1) migth be possible with plone.z3cform's FormExtender
    12:30 < rnix> datakurre: i was thinking of an IChildDefaultInstanceBehaviors behavior, which reads the available IInstanceBehavior deriving definitions. and sets them to
                  all added children by default
    12:30 < rnix> the add view can then be bound to IChildDefaultInstanceBehaviors
    12:31 < datakurre> rnix: Well, that works for sure.
    12:32 < rnix> datakurre: instead of binding the add view by name to Products.CMFCore.interfaces.IFolderish, we bind it to IChildDefaultInstanceBehaviors without name...


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


