#!/usr/bin/env python3

# Copyright Roger & Pep
# Factorial
# 15/08/22

# Español

import math

def title(): 
      
    print(
"""
 _____       _____     _      ____  _____   ___   ____  
| ____| ____|  ___|   / \    / ___||___  | / _ \ |  _ \ 
|  _|  |_  /| |_     / _ \  | |       / / | | | || |_) |
| |___  / / |  _|   / ___ \ | |___   / /  | |_| ||  _ < 
|_____|/___||_|    /_/   \_\ \____| /_/    \___/ |_| \_\\

                            Powered by the power of UwU
                            
                              |----------------------|
                              | Hecho por: Roger&Pep |
                              |----------------------|

Con este simple programa puedes 
factorizar cualquier numero que
quieras de una forma muy simple

Escribe 'q' para salir del programa

"""
)

    
def mirrorList(lst):
    
    mirrored = []
    
    for i in range(len(lst)-1, -1, -1):
        mirrored.append(lst[i])
    
    return mirrored

def numfact(n):
    
    factors = []
    
    n = float(n)
    
    if n == 0:
        print("Que haces tont@")

    elif n < 0:
        print("Me quieres cremar los circuitos?")

    elif n != int(n):
        print("Me ves con cara de tonta?")

    elif n == 69:
        print("23\n3\n1")
        print("\nJeje ;)")

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
        
        for num in factors:
            print(num)
        
    



def main():
    
    title()
    
    while True:

        print("Enter the number you want to factorize:")
        n = input('>> ')

        if n == "q" or n == "quit" or n == "exit":
            print("See you later, Alligator!")
            quit()

        else:
            numfact(n)

        
if __name__ == "__main__":
    main()
    
    
#   ;)
#
#   Roger&Pep
#
#
