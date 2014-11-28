#!/usr/bin/env python

from distutils.core import setup

setup(name='rdflib-appengine',
      version = '0.6',
      description='Python distributible for using rdflib with NDB',
      author='Niels Christensen',
      packages=['rdflib_appengine',
                ],
      install_requires=[
          'rdflib',
      ],
     )