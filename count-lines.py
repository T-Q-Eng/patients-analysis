"""This module counts the number of lines in standard input.
+ Input: A string from the system's standard input
+ Output: A the number of lines"""

import sys

count = 0

for line in sys.stdin:
	count+=1

print(count, "lines in standard input")

