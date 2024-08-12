#!/usr/bin/env python3
import sys

# Initiate variables
current_taxi = None
current_distance = 0.0
count = 0
taxi = None

# Read line from mapper
for line in sys.stdin:
    line = line.strip()
    taxi, distance = line.split(',')

    try:
        distance = float(distance)

    # Skip if cannot convert
    except ValueError:
        continue

    if current_taxi == taxi:

        # Count trips and add distance for the same taxi
        count += 1
        current_distance += distance

    else:

        # Print taxi number, trip, and average distance in 2 decimal format
        if current_taxi:
            avg_distance = current_distance/count
            print('%s,%s,%.2f' % (current_taxi, count, avg_distance))

        current_distance = distance
        current_taxi = taxi
        count = 1

# Print the last line
if current_taxi == taxi:
    avg_distance = current_distance/count
    print('%s,%s,%.2f' % (current_taxi, count, avg_distance))
