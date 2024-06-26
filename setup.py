from setuptools import find_packages
from setuptools import setup
import os


def read_file(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


version = "0.6.dev0"
shortdesc = "Enable behaviors per content type instance."
longdesc = '\n\n'.join([read_file(name) for name in [
    'README.rst',
    'CHANGES.rst',
    'LICENSE.rst'
]])


setup(
    name="collective.instancebehavior",
    version=version,
    description=shortdesc,
    long_description=longdesc,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.0",
        "Framework :: Plone :: Addon",
        "Framework :: Zope",
        "Framework :: Zope :: 5",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
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
