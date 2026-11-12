#!/bin/env python3

# print preamble
print('''
POCKET DICEWARE by Nycki, 2026

--------SYMBOLS/DIGITS--------  ------------------------------  ------------------------------  ------------------------------
11 1      31 "      51 <        Roll 18 dice: aaaa bb cccc dd eeee f g
12 2      32 '      52 =        - Look up the words for a, c, and e.
13 3      33 (      53 >        - Look up the symbols/digits for b and d.
14 4      34 )      54 ?        - Based on f, capitalize word a (1,4), c (2,5), or e (3,6).
15 5      35 *      55 @        - If a digit is required, use g directly.
16 6      36 +      56 [        - Example: 1234 56 2345 61 3456 1 2 -> AUNT[drunk]just2
21 7      41 ,      61 ]        - Haystack size: 6^16 * 3 = 8.46e12, approx. 2^43.
22 8      42 -      62 ^        
23 9      43 .      63 _        Alternate simple pattern: aaaa bbbb cccc dddd eeee
24 0      44 /      64 {        - Haystack size: 6^20 = 3.65e15, approx 2^52.
25        45 :      65 }        - Example: 1234 5612 2345 6123 4561 
26 !      46 ;      66 ~          -> aunt spot drunk suffer pink
''')

# with open("short-words.txt") as file:
#     words = [line.strip() for line in file]

with open("eff_short_wordlist_1.txt") as file:
    words = [line[4:].strip() for line in file]

blocks = []
for a in range(6):
    for b in range(6):
        lines = []
        lines.append(f'--------------{a+1}{b+1}--------------')
        for c in range(12):
            line = []
            for d in range(3):
                i = 216*a + 36*b + 12*d + c
                line.append(f'{2*d+c//6+1}{c%6+1} {words[i]:<6} ')
            lines.append(''.join(line))
        blocks.append(lines)

# print four blocks wide
for i in range(len(blocks)//4):
    for j in range(13):
        for k in range(4):
            print(blocks[4*i+k][j], end='  ')
        print()
    print()