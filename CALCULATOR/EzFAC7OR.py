# Copyright Roger & Pep
# Factorial
# 15/08/22

# Calculator

import math

# Main title of the project
def title():     
    print("EzFAC7OR-Roger&Pep")

    
    
# This function will mirror the final list 
# for example: with input ->["1", "2", "7"], will return ["7", "2", "1"]
def mirrorList(lst):
    mirrored = []

    for i in range(len(lst)-1, -1, -1):
        mirrored.append(lst[i])
    
    return mirrored

# Main function to factorize
def numfact(n):
    # Empty list where all the factors will be appended
    factors = []
    
    # Convert the value given to a float (to chech then for the easter eggs)
    n = float(n)
    
    # Easter eggs
    # 0, negative number, decimal number and 69 (for da jokes :P)

    if n == 0:
        print("What are you")
        print("doing silly?")

    elif n < 0:
        print("Do you want to")
        print("burn by circuits?")
 
    elif n != int(n):
        print("Do I look")
        print("stupid to you?")

    elif n == 69:
        print("23 3 1")
        print("Hehe ;)")

    ######################

    # Actual factorizing
    else:
        # Convert n to an integer (as n is a float)
        n = int(n)
        
        # Adds to the empty list the number 1
        factors = [1]
        
        # Adds all the 2s needed
        while n % 2 == 0:
            factors.append(2)
            n = n // 2
        
        # Applies factorizing formula
        for i in range(3, int(math.sqrt(n))+1, 2):
            while n % i == 0:
                factors.append(i)
                n = n // i
                
        if n > 2:
            factors.append(n)
        
        # The list gets mirrored (by the mirrorList() function)
        factors = mirrorList(factors)
        
        # Finally all the elements of the list gets joined in a same string | from ["7", "2", "1"] to "7 2 1"
        print(' '.join(str(num) for num in factors))
        
    
def main():
    
    # Prints the main title
    title()
    
    # Make a loop to factorize different numbers
    while True:
        print()
        print("Enter the number you")
        print("want to factorize:")
        n = input('>> ')

        if n == "q" or n == "quit" or n == "exit":
            print("See you later, Alligator!")
            quit()

        else:
            numfact(n)
        

        

main()
 

#    
#   ;)
#
#   Roger&Pep
#
#
