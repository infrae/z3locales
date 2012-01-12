from z3locales.i18n.locales import locales
from zope.i18n.interfaces import IUserPreferredLanguages

def normalize_lang(lang):
    lang = lang.strip().lower()
    lang = lang.replace('_', '-')
    lang = lang.replace(' ', '')
    return lang

def getlocaleinfo(self):
    return IUserPreferredLanguages(
        self.REQUEST).getPreferredLanguages() or ['en']


def getFormattedNow(self):
    from datetime import datetime
    import time
    now = time.gmtime()
    d = datetime(*now[:6])
    l = getlocaleinfo(self)[0]
    parts = l.split('-')
    formatter = locales.getLocale(*parts).dates.getFormatter('dateTime', 'full')
    return formatter.format(d)

__marker__ = []
def getFormattedDate(self, date, size="full", locale=__marker__, display_time=True):
    """return a formatted date

        date should be a tuple (year, month, day[, hour[, minute[, second]]])
    """
    from datetime import datetime
    d = datetime(*date)
    l = locale
    if l is __marker__:
        l = getlocaleinfo(self)[0]
    parts = l.split('-')
    format = 'dateTime'
    if not display_time:
      format = 'date'
    formatter = locales.getLocale(*parts).dates.getFormatter(format, size)
    return formatter.format(d)

def getMonthNames(self, locale=None, calendar='gregorian'):
    """returns a list of month names for the current locale"""
    l = locale
    if l is None:
        l = getlocaleinfo(self)[0]
    parts = l.split('-')
    return locales.getLocale(*parts).dates.calendars[calendar].getMonthNames()

def getMonthAbbreviations(self, locale=None, calendar='gregorian'):
    """returns a list of abbreviated month names for the current locale"""
    l = locale
    if l is None:
        l = getlocaleinfo(self)[0]
    parts = l.split('-')
    return locales.getLocale(*parts).dates.calendars[calendar].getMonthAbbreviations()
