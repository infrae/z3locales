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
"""Dummy Module

$Id: dummy.py,v 1.1 2004/11/30 17:33:39 guido Exp $
"""
from z3locales.interface import moduleProvides
from z3locales.interface.tests.ifoo import IFoo
from z3locales.interface import moduleProvides

moduleProvides(IFoo)

def bar(baz):
    pass
