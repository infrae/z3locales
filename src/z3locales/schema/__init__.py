##############################################################################
#
# Copyright (c) 2002 Zope Corporation and Contributors.
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
"""Schema package constructor

$Id: __init__.py,v 1.1 2004/11/30 17:33:39 guido Exp $
"""
from z3locales.schema._field import Field, Container, Iterable, Orderable
from z3locales.schema._field import MinMaxLen, Choice
from z3locales.schema._field import Bytes, ASCII, BytesLine
from z3locales.schema._field import Text, TextLine, Bool, Int, Float
from z3locales.schema._field import Tuple, List, Set
from z3locales.schema._field import Password, Dict, Datetime, Date, SourceText
from z3locales.schema._field import Object, URI, Id, DottedName
from z3locales.schema._field import InterfaceField
from z3locales.schema._schema import getFields, getFieldsInOrder
from z3locales.schema._schema import getFieldNames, getFieldNamesInOrder
from z3locales.schema.accessors import accessors
from z3locales.schema.interfaces import ValidationError
