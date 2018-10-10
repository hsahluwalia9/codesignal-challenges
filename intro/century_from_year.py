import math

def centuryFromYear(year):
    if year % 100 == 0:
        return year/100
    return math.floor((year/100) + 1)
