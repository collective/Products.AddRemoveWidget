from setuptools import setup, find_packages
import os

version = '1.5'

setup(name='Products.AddRemoveWidget',
      version=version,
      description="AddRemoveWidget + ComboBoxWidget for Plone",
      long_description=open(os.path.join("Products", "AddRemoveWidget", "README.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone",
        "Framework :: Zope2",
        ],
      keywords='Plone Archetypes Products AddRemoveWidget ComboBoxWidget',
      author='Martin Aspeli',
      author_email='optilude@gmx.net',
      url='http://plone.org/products/addremovewidget',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
