"""
NAME: Abhiram Aroop
STUDENT ID: 30632714
"""

import random
import math
import sys

#Computes the first n value in the m bit boundary
def get_n(m):
    return 2**(m-1)

#computes upper bound of n
def get_k(m):
    return 2**(m) - 1

#check part of miller rabin
def check(a,s,t,n):
    x =  pow(a,t,n)
    if x == 1:
        return True

    for i in range(s-1):
        if x == n-1:
            return True
        x = pow(x,2,n)
    return x == n-1


#checks if n is prime, boolean output (true if prime)
def millerRabinRandomisedPrimality(n,k):
    #special cases
    if n == 2 or n == 3:
        return True

    #remove all other even numbers as solutions
    if n % 2 == 0:
        return False

    s = 0
    t = n-1
    while t % 2 == 0:
        s += 1
        t = t//2

    #check the mod conditions for primality
    for i in range(k):
       a = random.randrange(2,n-1)
       if check(a,s,t,n) == False:
           return False
        
    return True

def check_twin_prime(m):
    n = get_n(m)
    k = get_k(m)

    #until twin prime found
    while True:
        rand_val = random.randrange(n,k)
        if millerRabinRandomisedPrimality(rand_val,k) is True:
            if millerRabinRandomisedPrimality(rand_val+2,k) is True and rand_val+2 <= k:
                return rand_val, rand_val+2
            if millerRabinRandomisedPrimality(rand_val-2,k) is True and rand_val-2 >= n:
                return rand_val-2,rand_val
            
def writeout(output):
        
    f = open("output_twin_prime.txt","w+")
    f.write(str(output[0]) + "\n" + str(output[1]))
    f.close()
    
if __name__ == "__main__":
    m = int(sys.argv[1])
    output = check_twin_prime(m)

    writeout(output)
    
    
    
        


