N=int(input())
H=int(input())
zemacena = 100000
for i in range(1, N+1, 1):
    P=int(input())
    C=int(input())
    saini = H//P
    cena = saini*C
    if cena<zemacena:
        zemacena=cena
print(zemacena)
