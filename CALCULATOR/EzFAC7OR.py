# Copyright Roger & Pep
# Factorial
# 15/08/22

# Calculator

import math

def title():     
    print("EzFAC7OR - Roger&Pep")

    
    
def mirrorList(lst):
    
    mirrored = []
    
    for i in range(len(lst)-1, -1, -1):
        mirrored.append(lst[i])
    
    return mirrored

def numfact(n):
    
    factors = []
    
    n = float(n)
    
    if n == 0:
        print("What are you doing silly")

    elif n < 0:
        print("Do you want to burn by circuits?")

    elif n != int(n):
        print("Do I look stupid to you?")

    elif n == 69:
        print("23 3 1")
        print()
        print("Hehe ;)")

    ######################

    else:
        n = int(n)
        
        factors = [1]
        
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
            
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                factors.append(i)
                n = n // i
                
        if n > 2:
            factors.append(n)
        
        factors = mirrorList(factors)
        
        print(' '.join(str(num) for num in factors))
        
    
def main():
    
    title()
    
    while True:
        print()
        print("Enter the number you want to factorize:")
        n = input('>> ')

        if n == "q" or n == "quit" or n == "exit":
            print("See you later, Alligator!")
            quit()

        else:
            numfact(n)

        

main()
    
    
#   ;)
#
#   Roger&Pep
#
#
