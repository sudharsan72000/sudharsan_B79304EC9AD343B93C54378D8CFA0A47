def isleap(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter a year: "))
if isleap(year):
  print("The leap year is {}".format(year))
else:
  print("Not leap year of {}".format(year))
