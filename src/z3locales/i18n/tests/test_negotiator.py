##############################################################################
#
# Copyright (c) 2001, 2002 Zope Corporation and Contributors.
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
"""Language Negotiator tests.

$Id: test_negotiator.py,v 1.1 2004/11/30 17:33:35 guido Exp $
"""
import unittest

from z3locales.i18n.negotiator import Negotiator
from z3locales.i18n.interfaces import IUserPreferredLanguages
from z3locales.component.tests.placelesssetup import PlacelessSetup
from z3locales.interface import implements

class Env(object):
    implements(IUserPreferredLanguages)

    def __init__(self, langs=()):
        self.langs = langs

    def getPreferredLanguages(self):
        return self.langs


class NegotiatorTest(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super(NegotiatorTest, self).setUp()
        self.negotiator = Negotiator()

    def test_findLanguages(self):

        _cases = (
            (('en','de'), ('en','de','fr'),  'en'),
            (('en'),      ('it','de','fr'),  None),
            (('pt-br','de'), ('pt_BR','de','fr'),  'pt_BR'),
            (('pt-br','en'), ('pt', 'en', 'fr'),  'pt'),
            (('pt-br','en-us', 'de'), ('de', 'en', 'fr'),  'en'),
            )

        for user_pref_langs, obj_langs, expected in _cases:
            env = Env(user_pref_langs)
            self.assertEqual(self.negotiator.getLanguage(obj_langs, env),
                             expected)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(NegotiatorTest),
                           ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
