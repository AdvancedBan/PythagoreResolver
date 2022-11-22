import math
import sys
import os
from decimal import Decimal

#PRESENT
print("PYTHAGORE :")
print("")
print("1 : Enter 1 if you want to calculate the hypotenuse :")
print("2 : Enter 2 if you want to calculate another length :")
print("")
print("")

#CHOICE
choice = input("Enter 1 or 2 >> ")
print("")

if choice == '1':

    #LONG
    A = input("Enter the first long >> ")
    B = input("Enter the second length >> ")
    #CARRE
    a1 = Decimal(f'{A}')
    b1 = Decimal(f'{B}')
    result_a1 = a1*a1
    result_b1 = b1*b1
    print(result_a1)
    print(result_b1)
    print("")

    #HYPOTENUSE
    a2 = Decimal(f'{result_a1}')
    b2 = Decimal(f'{result_b1}')
    result_ab = a2+b2

    #RACINE
    result_1 = (math.sqrt(result_ab))
    print("Result : ", result_1,"cm")

    
elif choice == '2':
    #LONG
    A = input("Enter the first long >> ")
    B = input("Enter the second length >> ")
    #CARRE
    a1 = Decimal(f'{A}')
    b1 = Decimal(f'{B}')
    result_a1 = a1*a1
    result_b1 = b1*b1
    print(result_a1)
    print(result_b1)
    print("")

    #HYPOTENUSE
    a2 = Decimal(f'{result_a1}')
    b2 = Decimal(f'{result_b1}')
    result_ab = a2-b2

    #RACINE
    result_2 = (math.sqrt(result_ab))
    print("Result : ", result_2,"cm")
else:
    print("The number you entered is not recognised !")


#RESTART
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("Do you want to restart this program ?")
    os.system('cls')
    if answer.lower().strip() in "y yes".split():
        restart_program()
