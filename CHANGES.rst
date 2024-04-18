Changes
=======

0.6 (unreleased)
----------------

- Drop Python 2 support.

- Do not invalidate global schema cache any more.

- Set _p_changed on object instances when enabling and disabling behaviors to
  ensure timestamp gets changed, which is used in plone 6 to look up schema
  from cache.


0.5
---

- Invalidate global schema cache [jensens]

- Black code style, isort imports, overall housekeeping [jensens]


0.4
---

- Be more explicit on dependencies and other egg improvements
  [tomgross]


0.3
---

- Fix ``DexterityInstanceBehaviorAssignable.enumerateBehaviors`` in order to
  work with plone.dexterity >= 2.3.0
  [agitator]


0.2
---

- convert behaviors in ``enable_behaviors`` to tuple before concat.
  [rnix]

- check whether instance behavior already in instance_behaviors before
  adding.
  [rnix]


0.1
---

- created ``collective.instancebehavior`` based on jcbrand's and thet's work
  [rnix]

- improved implementation with generic helper functions
  [thet]

- problem description and initial implementation
  [jcbrand]
