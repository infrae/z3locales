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
"""Interface field tests

$Id: test_interfacefield.py,v 1.1 2004/11/30 17:33:40 guido Exp $
"""
from unittest import main, makeSuite
from z3locales.schema import InterfaceField
from z3locales.schema.interfaces import RequiredMissing, WrongType
from z3locales.schema.tests.test_field import FieldTestBase
from z3locales.interface import Interface

class DummyInterface(Interface):
    pass

class InterfaceTest(FieldTestBase):
    """Test the Bool Field."""

    _Field_Factory = InterfaceField

    def testValidate(self):
        field = InterfaceField(title=u'Interface field', description=u'',
                     readonly=False, required=False)
        field.validate(DummyInterface)
        self.assertRaises(WrongType, field.validate, object())

    def testValidateRequired(self):
        field = InterfaceField(title=u'Interface field', description=u'',
                     readonly=False, required=True)
        self.assertRaises(RequiredMissing, field.validate, None)


def test_suite():
    return makeSuite(InterfaceTest)

if __name__ == '__main__':
    main(defaultTest='test_suite')
