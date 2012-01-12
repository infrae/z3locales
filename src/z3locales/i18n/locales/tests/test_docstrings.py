##############################################################################
#
# Copyright (c) 2004 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Tests for the ZCML Documentation Module

$Id: test_docstrings.py,v 1.1 2004/11/30 17:33:34 guido Exp $
"""
import unittest
from z3locales.testing.doctestunit import DocTestSuite
from z3locales.i18n.locales.inheritance import AttributeInheritance, NoParentException

class LocaleInheritanceStub(AttributeInheritance):

    def __init__(self, nextLocale=None):
        self.__nextLocale__ = nextLocale

    def getInheritedSelf(self):
        if self.__nextLocale__ is None:
            raise NoParentException, 'No parent was specified.'
        return self.__nextLocale__


def test_suite():
    return unittest.TestSuite((
        DocTestSuite('z3locales.i18n.locales'),
        DocTestSuite('z3locales.i18n.locales.inheritance'),
        DocTestSuite('z3locales.i18n.locales.xmlfactory'),
        ))

if __name__ == '__main__':
    unittest.main()