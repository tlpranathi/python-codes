def is_leap(yr):
    if yr%400 == 0 or yr%100 == 0 and yr%4 == 0:
        return True
    else:
        return True