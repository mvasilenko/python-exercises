#!/usr/bin/python3
import random

# class Knight:
#    def __init__(self, power=10, next=None):
#        self.power = power
#        self.next = next

knights = [{'power': 10, 'name': f'K{i}'} for i in range(1, 6+1)]
print(f"Initial knights list: {knights}")

i, next_i = 0, 1
while len(knights) > 1:
    damage = random.randrange(1, 6)
    print(f"damaging knight {knights[next_i]} with damage {damage}")
    knights[next_i]['power'] -= damage
    if knights[next_i]['power'] <= 0:
        print(f"killed knight {knights[next_i]}")
        knights = knights[:next_i] + knights[next_i+1:]
        print(f"New knights list: {knights}")

    i += 1
    if i >= len(knights):
        i = 0

    next_i = i+1
    if next_i >= len(knights):
        next_i = 0

print(f"Knight {knights[0]} is a winner")
