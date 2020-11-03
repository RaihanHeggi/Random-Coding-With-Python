def past(h, m, s):
    hoursToSecond = h * 3600
    minutesToSecond = m * 60
    miliSecond = (hoursToSecond + minutesToSecond + s) * 1000
    return miliSecond


print(past(1, 1, 1))

