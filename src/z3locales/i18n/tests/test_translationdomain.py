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
"""This module tests the regular persistent Translation Domain.

$Id: test_translationdomain.py,v 1.1 2004/11/30 17:33:35 guido Exp $
"""
import unittest, os
from z3locales.i18n.translationdomain import TranslationDomain
from z3locales.i18n.gettextmessagecatalog import GettextMessageCatalog
from z3locales.i18n.tests.test_itranslationdomain import \
     TestITranslationDomain, Environment
from z3locales.i18n import MessageIDFactory
from z3locales.i18n.interfaces import ITranslationDomain
from z3locales.component.servicenames import Utilities
from z3locales.component import getGlobalServices

def testdir():
    from z3locales.i18n import tests
    return os.path.dirname(tests.__file__)


class TestGlobalTranslationDomain(unittest.TestCase, TestITranslationDomain):

    def setUp(self):
        TestITranslationDomain.setUp(self)

    def _getTranslationDomain(self):
        domain = TranslationDomain('default')
        path = testdir()
        en_catalog = GettextMessageCatalog('en', 'default',
                                           os.path.join(path, 'en-default.mo'))
        de_catalog = GettextMessageCatalog('de', 'default',
                                           os.path.join(path, 'de-default.mo'))

        domain.addCatalog(en_catalog)
        domain.addCatalog(de_catalog)
        return domain

    def testNoTargetLanguage(self):
        # Having a fallback would interfere with this test
        self._domain.setLanguageFallbacks([])
        TestITranslationDomain.testNoTargetLanguage(self)

    def testSimpleNoTranslate(self):
        translate = self._domain.translate
        eq = self.assertEqual
        # Unset fallback translation languages
        self._domain.setLanguageFallbacks([])

        # Test that a translation in an unsupported language returns the
        # default, if there is no fallback language
        eq(translate('short_greeting', target_language='es'),
           None)
        eq(translate('short_greeting', target_language='es',
                     default='short_greeting'),
           'short_greeting')

        # Same test, but use the context argument instead of target_language
        context = Environment()
        eq(translate('short_greeting', context=context),
           None)
        eq(translate('short_greeting', context=context,
                     default='short_greeting'),
           'short_greeting')

    def testEmptyStringTranslate(self):
        translate = self._domain.translate
        self.assertEqual(translate(u'', target_language='en'), u'')
        self.assertEqual(translate(u'', target_language='foo'), u'')

    def testStringTranslate(self):
        self.assertEqual(
            self._domain.translate(u'short_greeting', target_language='en'),
            u'Hello!')

    def testMessageIDTranslate(self):
        factory = MessageIDFactory('default')
        translate = self._domain.translate
        msgid = factory(u'short_greeting', 'default')
        self.assertEqual(translate(msgid, target_language='en'), u'Hello!')
        # MessageID attributes override arguments
        msgid = factory('43-not-there', 'this ${that} the other')
        msgid.mapping["that"] = "THAT"
        self.assertEqual(
            translate(msgid, target_language='en', default="default",
                         mapping={"that": "that"}), "this THAT the other")

    def testMessageIDTranslateForDifferentDomain(self):
        domain = TranslationDomain('other')
        path = testdir()
        en_catalog = GettextMessageCatalog('en', 'other',
                                           os.path.join(path, 'en-default.mo'))
        domain.addCatalog(en_catalog)

        s = getGlobalServices().getService(Utilities)
        s.provideUtility(ITranslationDomain, domain, 'other')

        factory = MessageIDFactory('other')
        msgid = factory(u'short_greeting', 'default')
        self.assertEqual(
            self._domain.translate(msgid, target_language='en'), u'Hello!')

    def testSimpleFallbackTranslation(self):
        translate = self._domain.translate
        eq = self.assertEqual
        # Test that a translation in an unsupported language returns a
        # translation in the fallback language (by default, English)
        eq(translate('short_greeting', target_language='es'),
           u'Hello!')
        # Same test, but use the context argument instead of target_language
        context = Environment()
        eq(translate('short_greeting', context=context),
           u'Hello!')

    def testInterpolationWithoutTranslation(self):
        translate = self._domain.translate
        self.assertEqual(
            translate('42-not-there', target_language="en",
                      default="this ${that} the other",
                      mapping={"that": "THAT"}),
            "this THAT the other")


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestGlobalTranslationDomain))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(test_suite())
