#!/usr/bin/env python3
from collections import Counter

input_file = "./input_2.txt"


with open(input_file) as f:
    words = [l.strip() for l in f.readlines()]


three = 0
two = 0
for word in words:
    letter_count = [count for letter, count in Counter(word).most_common()]

    if 3 in letter_count:
        three += 1

    if 2 in letter_count:
        two += 1

print(two * three)
