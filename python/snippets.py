# Takes two lists and modifies the first to be the union of both
#union.union(list1,list2)
def union(a,b):
    
    for i in b:
        if  i not in a:
            a.append(i)
    a.sort
        
    return

# Lesson 3 Problem Set > Product List
# Define a procedure, product_list,
# takes as input a list of numbers,
# and returns a number that is
# the result of multiplying all
# those numbers together.

def product_list(p):
    ans = 1
    for i in p:
        ans = ans * i
    return ans

# Lesson 3 Problem Set > Greatest
# Define a procedure, greatest,
# that takes as input a list
# of positive numbers, and
# returns the greatest number
# in that list. If the input
# list is empty, the output
# should be 0.

def greatest(list):
    biggestSoFar = 0
    for i in list:
        if i > biggestSoFar:
            biggestSoFar = i
    return biggestSoFar

# Lesson 3 Problem Set > Lists of Lists
# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

def total_enrollment(p):
    
    totalCost = 0
    totalPop = 0
    for uni in p:
        totalPop += uni[1]
        totalCost += uni[1]*uni[2]
    return totalPop,totalCost

