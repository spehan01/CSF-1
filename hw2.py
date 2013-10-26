Enter file contents here# Name: Alex Sanders
# Evergreen Login: sanale04
# Computer Science Foundations
# Programming as a Way of Life
# HW2


# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.




from hw2_test import n



### Problem 1



# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"


answer = 0
i = 1


while i <= n:
        answer = answer + i
        i += 1
        print answer



### Problem 2


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"


for i in range(2, 11):
        print float(1) / float(i)



### Problem 3



# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"


n = 10
triangular = 0
for i in range(triangular, n + 1):    # Adding 1 because we start at 0
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n * (n + 1) / 2



### Problem 4


# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"


n = 10
answer = 1
for i in range(1, n+1):
        answer *= i
        print answer



### Problem 5



# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"


numlines = 10
answer = 1
i = numlines
while i > 0:
        for j in range(0, i):
                answer *= i - j
        print answer
        answer = 1
        i -= 1


### Problem 6

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


eulersNightmare = 1
for i in range(1, 10):
        fact = 1
        for j in range(0, i):
                fact *= i - j
        eulersNightmare += 1 / float(fact)
print eulersNightmare




### Collaboration

# Google was my best friend on this lol

### Reflection

#This was kinda hard. A lot of it was difficult, I spent a few hours on these problems. 
# I used google a lot to look up some of the loops and get more info, the lectures do help. 


