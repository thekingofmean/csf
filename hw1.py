# Name: Chris Edwards
# Evergreen Login: edwchr30
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


### I opted to add print lines to show the user what is going on behind the scenes.

###
### Problem 1
###

print "Problem 1 solution follows:"

# First we set our variables
a = 1
b = -5.86
c = 8.5408
print "a = 1"
print "b = -5.86"
print "c = 8.5408"
# This is the equation used to find the roots.
# Notice the slight difference between the two lines.
firstRoot = (-b +(math.sqrt(b*b-4*a*c)/(2*a)))
secondRoot = (-b -(math.sqrt(b*b-4*a*c)/(2*a)))

print "We find our first root with (-b +(math.sqrt(b*b-4*a*c)/(2*a)))"
print "and our second root with (-b -(math.sqrt(b*b-4*a*c)/(2*a)))"

# This will print the solution to our problem
print 'The first root is:'
print firstRoot
print 'The second root is:'
print secondRoot

###
### Problem 2
###

print "Problem 2 solution follows:"

# Here we use "execfile("filename") to add an external file,
# in this case setting a number of variables at once.

import hw1_test
### I'd like to "CAT" out the contents of hw1_test.py here, but don't know how yet.
print "hw1_test.py has been imported successfully."

###
### Problem 3
###

print "Problem 3 solution follows:"

# This uses the variables defined in hw1_test and prints out the following expression as a string

print "The expression we will evaluate is this: ((a^b)v(~c)^~(dvevf))"
print "Here is the result:"
print ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))



###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
