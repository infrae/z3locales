"""
    Example script for Zope 3's LocaleProvider, converts the current
    date to a local one using sys.argv[1] as the locale (falling back
    to 'en').

"""

# first some trickery to get this script to work from this location
import setpath
import os
os.chdir('src')

import sys, time
from src.z3locales.i18n.locales import provider
from datetime import datetime

locale = 'en'
if len(sys.argv) > 1:
    locale = sys.argv[1]

sub = None
if len(sys.argv) > 2:
    sub = sys.argv[2]

p = provider.LocaleProvider('z3locales/i18n/locales/data/')
if sub is None:
    l = p.getLocale(locale)
else:
    l = p.getLocale(locale, sub)
formatter = l.dates.getFormatter('dateTime')

now = time.gmtime()
d = datetime(*now[:6])
print formatter.format(d).encode('UTF-8')
