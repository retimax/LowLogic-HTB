#!/usr/bin/env python3

import csv

filename = 'input.csv'

rows = []
with open(filename, newline='') as f:
    lector = csv.reader(f, delimiter=',')
    header = next(lector)
    for f in lector:
        integers = [int(x) for x in f if x != '']
        rows.append(integers)

result = ''
for r in rows:
    int0, int1, int2, int3 = r
    and0 = int0 & int1
    and1 = int2 & int3
    xor_final = str(and0 | and1)
    result += xor_final

flag = ''
for i in range(0, len(result), 8):
    flag += chr(int(result[i:i+8], 2))
print(flag)
