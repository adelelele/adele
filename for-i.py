teksts = input()
vardi = teksts.split()
liel_sk=0
m=0
alfabetiko_sk=0
for vards in vardi:
    liel_sk=0
    m+=1
    k=0
    for i in range (len(vards)-1):
        if vards[i]>='A' and vards[i]<='Z':
            liel_sk+=1
        if vards[i]<vards[i+1]:
            k+=1
    if liel_sk == len(vards):
        print("visi lielie burti ir: ", m)
    print("Lielo burtu skaits vārdā: ", liel_sk)
    if k==len(vards)-1:  # skaitu veiksmīgos
        alfabetiko_sk+=1
if alfabetiko_sk==len(vardi):
    print("IR") 
       
        