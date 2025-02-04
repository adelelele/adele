n=int(input())
sak=int(input())
beig=int(input())

for i in range (2, n+1, 1):
    sak2=int(input())
    beig2=int(input())
    if sak>beig2 or sak2>beig:
        print("NE")
        break    
    if sak<=sak2:
        sak=sak2 
    if beig>=beig2:
        beig=beig2
        