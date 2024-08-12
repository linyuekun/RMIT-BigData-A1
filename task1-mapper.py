#!/usr/bin/env python3
import sys

# Read line, and split into fields
for line in sys.stdin:
    line = line.strip()
    field = line.split(',')

    try:
        # Capture taxi number (index 1) and distance (index 3), then print
        if field[1].strip() and field[3].strip():
            taxi_num = int(field[1])
            distance = float(field[3])
            print('%d,%f' % (taxi_num, distance))
    except:
        continue