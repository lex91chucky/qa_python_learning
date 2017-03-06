def is_year_leap(year):
    if ((year % 4 == 0) and (year % 100 > 0)) or (year % 400 == 0):
        a = True
    else:
        a = False
    return a
year = input("year = ")
year = int(year)
print(is_year_leap(year))
