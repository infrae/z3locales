##############################################################################
#
# Copyright (c) 2003 Zope Corporation and Contributors.
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
"""Message ID tests.

$Id: tests.py,v 1.1 2004/11/30 17:33:41 guido Exp $
"""
import unittest
from z3locales.testing.doctestunit import DocTestSuite

def test_suite():
    return DocTestSuite('z3locales.i18nmessageid.messageid')

if __name__ == '__main__':
    unittest.main(defaultTest="test_suite")
