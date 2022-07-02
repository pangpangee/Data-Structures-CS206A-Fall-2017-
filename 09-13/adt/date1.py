# date1.py
# implements the Date ADT
#

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

class Date():
  def __init__(self, year, month, day):
    self._year = year
    self._month = month
    self._day = day

  def year(self):
    return self._year

  def month(self):
    return self._month

  def day(self):
    return self._day

  def __str__(self):
    return "%04d/%02d/%02d" % (self._year, self._month, self._day)

  def _toJulianDay(self):
    tmp = 0
    if self._month < 3:
      tmp = -1
    return (self._day - 32075 + 
            (1461 * (self._year + 4800 + tmp) // 4) + 
            (367 * (self._month - 2 - tmp * 12) // 12) - 
            (3 * ((self._year + 4900 + tmp) // 100) // 4))

  def dayOfWeek(self):
    jday = self._toJulianDay()
    return jday % 7

  def numDays(self, otherDate):
    return otherDate._toJulianDay() - self._toJulianDay()

  def isLeapYear(self):
    return ((self._year % 400 == 0) or
            ((self._year % 4 == 0) and (self._year % 100 != 0)))

  def advanceBy(self, days):
    jday = self._toJulianDay() + days
    y, m, d = _jdayToYMD(jday)
    return Date(y, m, d)

