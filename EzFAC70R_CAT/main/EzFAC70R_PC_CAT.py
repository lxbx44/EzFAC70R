
# Copyright Roger & Pep (en menor mesura)
# Factorial
# 15/08/22


#Importar el mòdul de math per a poder realitzar operacións matemàtiques bàsiques
import math
#Importar el mòdul de art per a generar un títol
from art import *

#Introdució
tprint("EzFAC70R")
print("Powered by the power of UwU\n")

print("Amb aquest programari serà possible facotritzar el nombre desitjat amb facilitat!")
print("Escriu 'tancar' per finalitzar el programari! \n")
print("Fet per Roger&Pep\n")

#Funcions
def numfact(n):

    #Easter Eggs del programari
    n = float(n)
    if n == 0:
        print("Què fas tonto?")

    elif n < 0:
        print("Me vols cremar els circuits?")

    elif n != int(n):
        print("Em veus cara de tonta?")

    elif n == 69:
        print("3\n23\n1")
        print("\nJeje ;)")

        #Calculs matemàtics dels factors
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


#Loop principal
while True:
    #Input del nombre a factoritzar
    n = input('\nEntra el nombre a factoritzar: ')

    #Condició de tancar el programari -> Finalitzar
    if n == "tancar":
        print("Adeu marrameu!")
        quit()

    #Condició de continuar i executar el programari amb la funció principal
    else:
        numfact(n)


#   ;)
#
#   Roger&Pep
#
#
