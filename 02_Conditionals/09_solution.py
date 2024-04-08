year = int(input("give the year to check is leap or not :"))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print( year, " is a leap year")
else:
    print(year, "is NOT a leap year")