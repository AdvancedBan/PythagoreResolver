import math
import sys
import os
from decimal import Decimal

print("PYTHAGORE :")

A = input("Enter the first long >> ")
B = input("Enter the second length >> ")

#CARRE
a1 = Decimal(f'{A}')
b1 = Decimal(f'{B}')
result_a1 = a1*a1
result_b1 = b1*b1
print(result_a1)
print(result_b1)

#HYPOTENUSE
a2 = Decimal(f'{result_a1}')
b2 = Decimal(f'{result_b1}')
result_ab = a2+b2

#RACINE
print(math.sqrt(result_ab))

#RESTART
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

if __name__ == "__main__":
    answer = input("Do you want to restart this program ?")
    os.system('cls')
    if answer.lower().strip() in "y yes".split():
        restart_program()