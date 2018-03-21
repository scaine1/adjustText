#!/usr/bin/env python

from setuptools import setup

setup(name='adjustText_simon',
      version='0.6.1',
      description='Iteratively adjust text position in matplotlib plots to minimize overlaps',
      author='Ilya Flyamer',
      author_email='flyamer@gmail.com',
      url='https://github.com/Phlya/adjustText',
      packages=['adjustText_simon'],
      install_requires=['numpy', 'matplotlib']
     )
