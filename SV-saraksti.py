augli = {"ananas", "banans", "mango", "papaija", "abols"}
augli.add("pasiflora")
garvards = len(max(augli, key=len))
print(garvards) 
ir1=0
isakaisv=1000000
saraksts = list(augli)
gariaugli= { }
for i in range (len(saraksts)):
    if saraksts[i]=="papaja" or saraksts[i]== "karambola":
        ir1+=1
    if len(saraksts[i])>=5:
        gariaugli.add(saraksts[i])
    if saraksts[i]<isakaisv:
        isakaisv=saraksts[i]
if ir1==1:
    print("IR VISMAZ VIENA")
else:
    print("VISMAZ VIEN NAV")    
