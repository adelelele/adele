import math

Ax=int(input())
Ay=int(input())
R=int(input())
hipo=Ax**2+Ay**2
if hipo < R**2:
    print("Ir iekšā")
elif hipo > R**2 : 
    print("Nav iekšā")
else:
    print("Uz riņķa līnijas")