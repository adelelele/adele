import math
Ax = int(input())
Ay = int(input())
Bx = int(input())
By = int(input())
Cx = int(input())
Cy = int(input())
ab=((Ax-Bx)**2+(Ay+By)**2)
ac =((Ax-Cx)**2+(Ay+Cy)**2)
bc =((Bx-Cx)**2+(By+Cy)**2)
if ab>ac and ab>bc:
    garakais = ab
    isais1 = ac
    isais2 = bc
elif bc>ac and bc>ab:
    garakais = bc
    isais1 = ac
    isais2 = ab
else: 
    garakais = ac
    isais1 = bc 
    isais2 = ab
    
    
if garakais == isais1+isais2:
    print("ir taisnleņķis")
else: 
    print("nav")