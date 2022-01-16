import random
numberOfStreaks = 0
ones = ['1'] * 6
zeros = ['0'] * 6
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    l = []
    for i in range(0, 100):
        l.append(str(random.randint(0, 1)))
    # Code that checks if there is a streak of 6 heads or tails in a row.
    if ''.join(zeros) in ''.join(l) or ''.join(ones) in ''.join(l):
        numberOfStreaks += 1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
