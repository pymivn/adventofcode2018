# Part 1
with open('day2_input.txt') as f:
    lines = [line.strip() for line in f]

from collections import Counter 
twos = 0
threes = 0
for line in lines:
    if 2 in set(Counter(line).values()):
        twos += 1
    if 3 in set(Counter(line).values()):
        threes += 1
print(twos, threes, twos*threes)

# Part 2
with open('day2_input.txt') as f:
    lines = [line.strip() for line in f]

for idx, line in enumerate(lines[:-1]):
    for other_line in lines[idx+1:]:
        different_chars = [c for idx, c in enumerate(line) if c != other_line[idx]]
        if len(different_chars) == 1:
            print(line, other_line)
            common_chars = ''.join(c for idx, c in enumerate(line) if c == other_line[idx])
            print(common_chars)
            break
