# Name: Alex Sanders
# Evergreen Login: sanale04
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408
x1=(-b+math.sqrt(b**2-4*a*c))/(2*a)
x2=(-b-math.sqrt(b**2-4*a*c))/(2*a)

print "x1=",x1,"x2=", x2

print "Problem 2 solution follows:"

from hw1_test import a,b,c,d,e,f

print a,b,c,d,e,f



print "Problem 3 solution follows:"


print "answer=",((a and b) or (not c) and not (d or e or f)) 

##Micah, Jason, Brandon 

#taught me a shorter way to do problems 2 and 3, thanks!
