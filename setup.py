from setuptools import find_packages
from setuptools import setup

import os


version = "0.5"
shortdesc = "Enable behaviors per content type instance."
longdesc = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
longdesc += open(os.path.join(os.path.dirname(__file__), "CHANGES.rst")).read()
longdesc += open(os.path.join(os.path.dirname(__file__), "LICENSE.rst")).read()


setup(
    name="collective.instancebehavior",
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: 5.1",
        "Framework :: Plone :: 5.2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    author="JC Brand, Johannes Raggam, Robert Niederreiter",
    author_email="",
    keywords="Python Plone Dexterity Behavior Development",
    license="GNU General Public Licence",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://pypi.python.org/pypi/collective.instancebehavior",
    namespace_packages=["collective"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.behavior",
        "plone.dexterity",
        "zope.annotation",
        "zope.component",
        "zope.interface",
    ],
    extras_require={"test": ["plone.app.testing",]},
    entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
