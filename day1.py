# Part 1
with open('day1_input.txt') as f:
        print(sum(int(line) for line in f))

# Part 2
from itertools import cycle
with open('day1_input.txt') as f:
    lines = f.readlines()
changes = cycle(int(line) for line in lines)
freqs = [0]

for c in changes:
    new_freq = freqs[-1] + c
    if new_freq in freqs:
        print(new_freq)
        break
    else:
        freqs.append(new_freq)
