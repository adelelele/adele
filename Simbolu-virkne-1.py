virkne1=input()
burtsk=0
vardi=virkne1.split()
if virkne1[-1]=='?':
    print("Jautājuma teikums")
elif virkne1[-1]=='!':
    print("Rosinājuma teikms")
else: 
    print("Stāstījuma teikums")
#izvada kāda veida teikums^
print(virkne1.count(" ") + 1)
#izvada cik vārdi teikumā^
for i in range (len(virkne1)):
    if virkne1[i]==' ':
        print(virkne1[i-1])
print(virkne1[-2])
#izvada vārdu pēdējos burtus^
for o in range(len(vardi)-1):
    print(len(vardi[o]))
print(len(vardi[len(vardi)-1])-1)
#izvada visu vārdu garumus^
for p in range(len(vardi)):
    