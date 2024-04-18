Using the development buildout
------------------------------

Create a virtualenv in the package::

    $ virtualenv --clear .

Install requirements with pip::

    $ ./bin/pip install -r requirements.txt

Run buildout::

    $ ./bin/buildout

Start Plone in foreground:

    $ ./bin/instance fg


IRC log
-------

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
