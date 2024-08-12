#!/usr/bin/env python3
import sys

# Read line, and split into fields
for line in sys.stdin:
    line = line.strip()
    field = line.split(',')

    # Check which file the line comes from by the number of columns
    # Then print the result with '-' for missing value

    # This is from Taxis.txt
    if len(field) == 4:
        taxi_num = int(field[0].strip())
        company = int(field[1].strip())
        print('%d,%d,%s' % (taxi_num, company, '-'))

    # This is from Trips.txt
    else:
        taxi_num = int(field[1].strip())
        trip_num = int(field[0].strip())
        print('%d,%s,%d' % (taxi_num, '-', trip_num))
