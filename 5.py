#!/usr/bin/env python3
# Thanks reddit user u/andreyrmg for this elegant solution, keeping it here so I can learn from it
#
from string import ascii_lowercase


def collapse(s):
    polymers = ['.']

    for letter in s:
        last_letter = polymers[-1]

        # If the letter before is not exactly the same BUT if we change it to lowe case its a match
        if last_letter != letter and last_letter.lower() == letter.lower():
            polymers.pop()
        else:
            polymers.append(letter)

    # Remove one from length because of the added dot
    return len(polymers) - 1


with open('./input_5.txt') as f:
    puzzle = f.read().strip()

print(collapse(puzzle))

# Test all combinations where you remove a character from the alphabet and check for the shortest string
print(min(collapse(c for c in puzzle if c.lower() != l) for l in ascii_lowercase))
