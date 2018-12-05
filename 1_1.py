#!/usr/bin/env python3
import operator

input_file = "./input_1.txt"
result = 0

operators = {
    "+": operator.iadd,
    "-": operator.isub
}

with open(input_file) as f:
    for number in f:
        operator = operators[number[:1]]
        number = int(number[1:])
        result = operator(result, number)

print("final result is: %d" % result)
