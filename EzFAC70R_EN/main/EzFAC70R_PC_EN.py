
# Copyright Roger & Pep
# Factorial
# 15/08/22


#Import the math module for simple mathematical instructions
import math
#Import the art module for generating the title
from art import *

#Introdució
tprint("EzFAC70R")
print("Powered by the power of UwU\n")

print("With this simple program, you can factorize any number you whant in a simple way!")
print("Write 'quit' to quit the program\n")
print("Made by: Roger&Pep\n")

#Functions
def numfact(n):

    #Project's Easter Eggs
    n = float(n)
    if n == 0:
        print("What are you doing silly")

    elif n < 0:
        print("Do you want to burn by circuits?")

    elif n != int(n):
        print("Do I look stupid to you?")

    elif n == 69:
        print("3\n23\n1")
        print("\nHehe ;)")

        #Mathematical operations
    else:
        while n % 2 == 0:
            print(2)
            n = n / 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                print(i)
                n = n / i

        if n > 2:
            n = int(n)
            print(f"{n}\n1")


#Main loop
while True:
    #The input of the number to factorize
    n = input('\nEnter the number you want to factorize: ')

    #Closing program's condition
    if n == "quit":
        print("See you later, Alligator!")
        quit()

    #Execute the main function's condition
    else:
        numfact(n)


#   ;)
#
#   Roger&Pep
#
#
