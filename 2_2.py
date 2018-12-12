#!/usr/bin/env python3

input_file = "./input_2.txt"

with open(input_file) as f:
    words = f.read().splitlines()


# Compare each item in list with the rest once for every word in list
for word in range(len(words)):
    for next_word in range(word + 1, len(words)):
        _word = words[word]
        _next_word = words[next_word]

        # Input are words of the same length (otherwise a length check would be in place here)
        diff = 0
        for l_word, l_next_word in zip(_word, _next_word):
            if l_word != l_next_word:
                diff += 1

                if diff > 1:
                    break

        if diff == 1:
            correct_word = [letter for letter, next_letter in zip(_word, _next_word) if letter == next_letter]
            print(''.join(correct_word))
