def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year == 1800 or 1900 or 2100 or 2200 or 2300 or 2500:
            leap = False
        else:
            leap = True
    else:
        leap = False
    return leap


year = int(input())
print(is_leap(year))