#!/usr/bin/env python3
import sys

# Read line, and split into fields
for line in sys.stdin:
    line = line.strip()
    field = line.split(',')
    company = int(field[0].strip())
    count = int(field[1].strip())

    print('%d,%d' % (company, count))

