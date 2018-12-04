# Part 1
with open('day1_input.txt') as f:
        print(sum(int(line) for line in f))

# Part 2
from itertools import cycle
with open('day1_input.txt') as f:
    lines = f.readlines()
changes = cycle(int(line) for line in lines)
last_freq = 0
freqs = set()

for c in changes:
    new_freq = last_freq + c
    if new_freq in freqs:
        print(new_freq)
        break
    else:
        freqs.add(new_freq)
        last_freq = new_freq
