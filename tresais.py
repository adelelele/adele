h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())
startas=h1*3600+60*m1+s1
beigus=3600*h2+60*m2+s2
cikilgi=beigus-startas
st=cikilgi//3600
min=(cikilgi-st*3600)//60
sek=cikilgi-st*3600-min*60
print(st, "h", min, "min", sek, "sek")