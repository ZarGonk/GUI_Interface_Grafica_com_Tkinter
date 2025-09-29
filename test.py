def show_days(op=0):
    days = []
    if op == 1: days.append('Sunday')
    if op == 2: days.append('Monday')
    if op == 3: days.append('Tuesday')
    if op == 4: days.append('Wednesday')
    if op == 5: days.append('Thursday')
    if op == 6: days.append('Saturday')

    return days

test = show_days(3)
test = show_days(4)

print(test)

