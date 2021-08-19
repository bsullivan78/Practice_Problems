#   https://www.codewars.com/kata/5226eb40316b56c8d500030f/python
#   previous version did not imoprt math and used custom factorial function

import math

def pascals_triangle(n):
    a = [1]
    for i in range(1,n):
        for k in range(0,i+1):
            print("i: " + str(i) + " k: " + str(k) + " l: " + str(calc(i,k)) )
            a.append( calc(i,k) )
    return a
    
def calc(n,k):
    if((k == 0)or (k == n)):
        return 1
    else:  
        return ( math.factorial(n) )//( math.factorial(k) * math.factorial(n-k) )  # Floor division is absolutely required
