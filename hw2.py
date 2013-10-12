# Name: Alex Sanders    
# Evergreen Login: Sanale04
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

#Imports
from fractions import Fraction
from hw2_test import n


### Problem 1


print "Problem 1 solution follows:"


sum = 0
i = 0
while i <= n:
    sum = sum + i
    print sum
    i = i + 1
    
    
    
    

### Problem 2


print "Problem 2 solution follows:"

base = 1.0  
count = 1.0  
  
for num in range(0,10):  
        base = base / count       
        print base   
        count = count + 1.0  
        base = 1.0  



### Problem 3


print "Problem 3 solution follows:"

n = 1
triangular = 0
for i in range(0,10):
    triangular = triangular + i
    print "Triangular number", n, "via loop:", triangular
    print "Triangular number", n, "via formula:", n*(n+1)/2
    n = n + 1


### Problem 4



print "Problem 4 solution follows:"

a = 1
b = 1
for i in range(1,11):
    b = b + i 
    print "Factorial number", a, "via loop:", b
    a += 1
###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

# ... write your code and comments here (and remove this line)

###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
