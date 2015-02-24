#!/usr/bin/python

import math
import sys
import time

# This thing, F O R C E M A T R I X, is just a calculator function code snippet.
# Take an input file called /usr/local/lib/forcematrix.in and have it contain line delimited base 10 numbers.
# F O R C E M A T R I X will run a series of simple calculations on numbers 1 through the value in the file.
# If you use multiple lines, you will run the calulation again, 1 through the next value. The values from the file are
# F O R C E M A T R I X run ranges.

# Example simple usage:
# echo 9999 > /usr/local/lib/forcematrix.in
# /usr/local/scripts/forcematrix.py
#
# Example advanced usage:
# for x in {1..99999}; do echo "$x" > /usr/local/lib/forcematrix.in &&
# /usr/local/scripts/forcematrix.py > /mnt/hadoop2/node-a-in-raw-matrix/forcematrix.out;
# done

f = (open("/usr/local/lib/forcematrix.in"))

# Start the clock!
start_time = time.clock()

# Crunch those numbers.
for line in f:
  x = line
  y = int(line)
  type(y)
  print ' '
  print 'FORCEMATRIX: calculating for 1 through', line
  for x in range(1, y+1):
        print repr(x), repr(x*x), repr(x*y), repr(x^10), repr(x^y), repr(x*60), repr(x*24), repr(x*7), repr(x*12), repr(x*x*y), repr(x*y*y), repr(x*x*y*y), repr(x*x*x^y), repr(x*x*x*x^y^y),repr(x**2), repr(x**3), repr(x**4)
print ' '
print 'forcematrix just crunched out the following operations for each range from the input file in',
print time.clock() - start_time, "seconds"
# Put whatever operations you want in here. This is just a set I'm using for load testing. 
# Try using just XOR or just multiplication and see how the timing compairs.
print 'x x*x x*y x^10 x^y x*60 x*24 x*7 x*12 x*x*y x*y*y x*x*y*y x*x*x^y x*x*x*x^y^y x**2 x**3 x**4'
