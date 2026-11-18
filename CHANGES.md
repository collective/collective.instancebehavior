# Changes

<!-- towncrier release notes start -->

## 0.6 (unreleased)

- Drop Python 2 support.

- Do not invalidate global schema cache any more.

- Set _p_changed on object instances when enabling and disabling behaviors to
  ensure timestamp gets changed, which is used in plone 6 to look up schema
  from cache.

- Breaking: replace the `pkg_resources` namespace of `collective` with a
  PEP 420 native namespace. Support Plone 6.1 on Python 3.10 to 3.13, and
  Plone 6.2 on Python 3.10 to 3.14. Use 0.5 for older Plone versions and
  Python 2.7.
  [remdub]

- Declare `transaction` as a dependency: the helpers import it.
  [remdub]

- Add tests for `enable_behaviors`, `disable_behaviors`,
  `instance_behaviors_of` and the behavior assignable.
  [remdub]

- Configure the package with plone.meta 2.12.0 (test matrix on Plone 6.2.3
  and 6.1), move its metadata to `pyproject.toml`, convert the documentation
  to Markdown and run the development environment on Plone 6.2.3 with uv
  instead of buildout.
  [remdub]


## 0.5

- Invalidate global schema cache [jensens]

- Black code style, isort imports, overall housekeeping [jensens]


## 0.4

- Be more explicit on dependencies and other egg improvements
  [tomgross]


## 0.3

- Fix `DexterityInstanceBehaviorAssignable.enumerateBehaviors` in order to
  work with plone.dexterity >= 2.3.0
  [agitator]


## 0.2

- convert behaviors in `enable_behaviors` to tuple before concat.
  [rnix]

- check whether instance behavior already in instance_behaviors before
  adding.
  [rnix]


## 0.1

- created `collective.instancebehavior` based on jcbrand's and thet's work
  [rnix]

- improved implementation with generic helper functions
  [thet]

- problem description and initial implementation
  [jcbrand]
