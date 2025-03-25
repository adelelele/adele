teikums = input()
vardi = teikums.split()
m = 0
ir3 = 0
for vardi in teikums (len(teikums)):
    for i in range (len(vards)):
        if vards[i]>='a' and vards[i]<='z' or vards[i]>='A' and vards[i]<='Z':
            m+=1
    if m==3:
        ir3+=1
    if m%2==0:
        paravardi=teikums[vardi]
    
if ir3>0:
    print("IR 3 SIMBOLI")
else:
    print("NAV 3 SIMBOLI")