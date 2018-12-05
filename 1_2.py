#!/usr/bin/env python3
from operator import iadd, isub
from itertools import cycle

input_file = "./input_1.txt"

operators = {
    "+": iadd,
    "-": isub
}

seen = {0}
frequency = 0
with open(input_file) as f:
    for number in cycle(f):
        operator = operators[number[:1]]
        number = int(number[1:])
        frequency = operator(frequency, number)

        if frequency in seen:
            print("frequency is: %d" % frequency)
            break

        seen.add(frequency)
