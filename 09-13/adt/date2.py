# date2.py
# implements the Date ADT
# with a smaller Date object containing only the Julian day number

def _jdayToYMD(jday):
  A = jday + 68569
  B = 4 * A // 146097
  A = A - (146097 * B + 3) // 4
  year = 4000 * (A + 1) // 1461001
  A = A - (1461 * year // 4) + 31
  month = 80 * A // 2447
  day = A - (2447 * month // 80)  
  A = month // 11
  month = month + 2 - (12 * A)
  year = 100 * (B - 49) + year + A
  return year, month, day

def _toJulianDay(year, month, day):
  tmp = 0
  if month < 3:
    tmp = -1
  return (day - 32075 + 
          (1461 * (year + 4800 + tmp) // 4) + 
          (367 * (month - 2 - tmp * 12) // 12) - 
          (3 * ((year + 4900 + tmp) // 100) // 4))
  
class Date():
  def __init__(self, year, month, day):
    self._jday = _toJulianDay(year, month, day)

  def _toYMD(self):
    return _jdayToYMD(self._jday)

  def year(self):
    return self._toYMD()[0]

  def month(self):
    return self._toYMD()[1]

  def day(self):
    return self._toYMD()[2]

  def __str__(self):
    y, m, d = self._toYMD()
    return "%04d/%02d/%02d" % (y, m, d)

  def dayOfWeek(self):
    return self._jday % 7

  def numDays(self, otherDate):
    return otherDate._jday - self._jday

  def isLeapYear(self):
    y = self.year()
    return ((y % 400 == 0) or
            ((y % 4 == 0) and (y % 100 != 0)))

  def advanceBy(self, days):
    y, m, d = _jdayToYMD(self._jday + days)
    return Date(y, m, d)

