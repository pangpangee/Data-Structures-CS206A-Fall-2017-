#
# Day calculator:
# now with checking of dates
#

from date4 import Date

monthNames = [ "January", "February", "March", "April",
               "May", "June", "July", "August",
               "September", "October", "November", "December" ]
dayNames = [ "Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday" ]
digits = "0123456789"

def get_date(s):
  if len(s) != 10 or s[4] not in "/.-" or s[7] != s[4]:
    raise ValueError("Incorrect date format")
  for i in range(10):
    if i != 4 and i != 7 and s[i] not in digits:
      raise ValueError("Incorrect date format")
  year = int(s[:4])
  month = int(s[5:7])
  day = int(s[8:])
  return Date(year, month, day)

def show_weekday(s):
  day = get_date(s)
  print(day, "is a", dayNames[day.dayOfWeek()])

def show_difference(s1, s2):
  day1 = get_date(s1)
  day2 = get_date(s2)
  print("There are", day1.numDays(day2), "days between", day1, "and", day2)

def show_advance(s1, op, s2):
  day = get_date(s1)
  n = int(s2)
  if op not in "+-":
    print("Incorrect operator (only plus and minus are possible)")
    return
  m = n
  if op == "-":
    m = -n
  print(day, op, n, "days =", day.advanceBy(m))
    
def main():
  print("Welcome to the CS206 day calculator\n")
  print("You can do the following:")
  print(" * Enter a date to determine the weekday")
  print(" * Enter two dates to determine the number of days in between")
  print(" * Enter a date, + or -, and then a number of days\n")
  print("All dates are in the form YYYY/MM/DD\n")

  while True:
    s = input("> ")
    f = s.split()
    try:
      if len(f) == 0:
        return
      elif len(f) == 1:
        show_weekday(f[0])
      elif len(f) == 2:
        show_difference(f[0], f[1])
      elif len(f) == 3:
        show_advance(f[0], f[1], f[2])
      else:
        print("Incorrect command")
    except ValueError as e:
      print(e)

main()
