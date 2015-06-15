#!/usr/bin/env python

from setuptools import setup

if __name__ == '__main__':
    setup(
          name = 'buglist',
          version = '1.0.dev0',
          description = '''''',
          long_description = '''''',
          author = "",
          author_email = "",
          license = '',
          url = '',
          scripts = ['scripts/bug~', 'scripts/bug'],
          packages = [],
          py_modules = ['__init__', 'bugzilladb', 'bug'],
          classifiers = ['Development Status :: 3 - Alpha', 'Programming Language :: Python'],
          entry_points={
          'console_scripts':
              []
          },
             #  data files
             # package data
          
          
          zip_safe=True
    )
