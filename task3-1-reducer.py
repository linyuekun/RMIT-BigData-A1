#!/usr/bin/env python3
import sys

# Initiate variables
current_taxi = None
count = 0

# Read line from mapper
for line in sys.stdin:
    line = line.strip()
    taxi_num, company, trip_num = line.split(',')

    # Count lines from Trips.txt
    if current_taxi == taxi_num and trip_num != '-':
        count += 1

    else:
        # Print company and total trips if from Taxis.txt
        if current_taxi and company != '-':
            print('%s,%s' % (company, count))

        current_taxi = taxi_num
        count = 1

