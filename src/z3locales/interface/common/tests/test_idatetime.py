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
"""Test for datetime interfaces

$Id: test_idatetime.py,v 1.1 2004/11/30 17:33:38 guido Exp $
"""

import unittest

from z3locales.interface.verify import verifyObject, verifyClass
from z3locales.interface.common.idatetime import ITimeDelta, ITimeDeltaClass
from z3locales.interface.common.idatetime import IDate, IDateClass
from z3locales.interface.common.idatetime import IDateTime, IDateTimeClass
from z3locales.interface.common.idatetime import ITime, ITimeClass, ITZInfo
from datetime import timedelta, date, datetime, time, tzinfo

class TestDateTimeInterfaces(unittest.TestCase):

    def test_interfaces(self):
        verifyObject(ITimeDelta, timedelta(minutes=20))
        verifyObject(IDate, date(2000, 1, 2))
        verifyObject(IDateTime, datetime(2000, 1, 2, 10, 20))
        verifyObject(ITime, time(20, 30, 15, 1234))
        verifyObject(ITZInfo, tzinfo())
        verifyClass(ITimeDeltaClass, timedelta)
        verifyClass(IDateClass, date)
        verifyClass(IDateTimeClass, datetime)
        verifyClass(ITimeClass, time)


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestDateTimeInterfaces))
    return suite


if __name__ == '__main__':
    unittest.main()
