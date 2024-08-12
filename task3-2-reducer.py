#!/usr/bin/env python3
import sys

# Initiate variables
current_company = None
total_count = 0

# Read line from mapper
for line in sys.stdin:
    line = line.strip()
    company, count = line.split(',')

    # If it is the same company, sum up
    if current_company == company:
        total_count = int(total_count)
        count = int(count)
        total_count += count

    else:
        # If it is another company, print the result and move on to set up a new pair
        if current_company:
            print('%s,%s' % (current_company, total_count))

        # Set both variables to the values in the line
        current_company = company
        total_count = count

