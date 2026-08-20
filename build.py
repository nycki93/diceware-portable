#!/bin/env python3

with open("short-words.txt") as file:
    words = [line.strip() for line in file]
print(len(words))

blocks = []
for a in range(6):
    for b in range(6):
        lines = []
        lines.append(f'--------------{a+1}{b+1}-------------- ')
        for c in range(12):
            line = []
            for d in range(3):
                i = 216*a + 36*b + 12*d + c
                line.append(f'{2*d+c//6+1}{c%6+1} {words[i]:<6}')
            lines.append(' '.join(line))
        block = '\n'.join(lines)
        print(block)