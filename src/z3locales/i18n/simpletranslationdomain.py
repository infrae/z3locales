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
"""This is a simple implementation of the ITranslationDomain interface.

$Id: simpletranslationdomain.py,v 1.1 2004/11/30 17:33:10 guido Exp $
"""
from z3locales.interface import implements
from z3locales.component import getUtility
from z3locales.i18n.interfaces import ITranslationDomain, INegotiator
from z3locales.i18n import interpolate

class SimpleTranslationDomain(object):
    """This is the simplest implementation of the ITranslationDomain I
       could come up with.

       The constructor takes one optional argument 'messages', which will be
       used to do the translation. The 'messages' attribute has to have the
       following structure:

       {('language', 'msg_id'): 'message', ...}

       Note: This Translation Domain does not use message catalogs.
    """
    implements(ITranslationDomain)

    # See z3locales.i18n.interfaces.ITranslationDomain
    domain = None

    def __init__(self, domain, messages=None):
        """Initializes the object. No arguments are needed."""
        self.domain = domain
        if messages is None:
            self.messages = {}
        else:
            assert isinstance(messages, dict)
            self.messages = messages


    def translate(self, msgid, mapping=None, context=None,
                  target_language=None, default=None):
        '''See interface ITranslationDomain'''
        # Find out what the target language should be
        if target_language is None and context is not None:
            langs = [m[0] for m in self.messages.keys()]
            # Let's negotiate the language to translate to. :)
            negotiator = getUtility(INegotiator)
            target_language = negotiator.getLanguage(langs, context)

        # Find a translation; if nothing is found, use the default
        # value
        text = self.messages.get((target_language, msgid))
        if text is None:
            text = default
        return interpolate(text, mapping)
