#!/usr/bin/env python3
from string import ascii_uppercase


def create_dict():
    new_dict = dict()

    for letter in ascii_uppercase:
        new_dict[letter] = []

    return new_dict


def sort_dict(d):
    for key in d:
        d[key].sort()
    return d


def parse_input(instructions):
    prereq = create_dict()

    for line in instructions:
        line = line.split('Step ')[1].split(' must be finished before step ')
        first_step = line[0]
        next_step = line[1].split(' can begin.')[0]

        # Prereq contains all steps that must be completed before the current step can begin
        prereq[next_step].append(first_step)

    sort_dict(prereq)

    return prereq


with open('./input_7.txt') as f:
    instructions = f.read().splitlines()

prereq = parse_input(instructions)
step_order = list()

while prereq:
    for step, prereq_steps in prereq.items():
        # If step is missing any prerequsite steps, its ready to go. Input is already sorted.
        if not prereq_steps:
            step_order.append(step)

            # Remove the step as a prereq since it's executed
            for key in prereq.keys():
                if step in prereq[key]:
                    prereq[key].remove(step)

            # Remove the step from prereq dict since we are done with it
            prereq.pop(step)
            break


print(''.join(step_order))
