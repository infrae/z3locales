# Copyright (c) 2004-2008 Infrae. All rights reserved.
# See also LICENSE.txt
# $Id$

from setuptools import setup, find_packages
import os

version = '0.2'

setup(name='z3locales',
      version=version,
      description="Common Python library which contains reusable components, developed at Infrae.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
              "Framework :: Zope2",
              "Framework :: Zope3",
              "License :: OSI Approved :: Zope Public License",
              "Topic :: Software Development :: Internationalization",
              "Programming Language :: Python",
              "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='internationalization zope2 zope3 i18n',
      author='Infrae',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='ZPL 2.1',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir = {'': 'src'},
      include_package_data=True,
      zip_safe=True,
      test_suite = 'localdatetime.tests.test_suite',
      install_requires=[
          'zope.i18n',
          'DateTime',
          ],
      )
