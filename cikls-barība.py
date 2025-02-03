K=int(input())
N=int(input())

mazi_cena=1000000
mazi_maisi=100000
for i in range(1,N+1,1):
    M=int(input())
    C=int(input())
    razotajs=input()
    if razotajs!="DOGO":
        cena_pa_kg=C/M
        cik_var_atlauties=K//C
        if cena_pa_kg< mazi_cena:
            razotajs2=razotajs
            mazi_maisi=cik_var_atlauties
            mazi_cena=cena_pa_kg
print(razotajs2, mazi_maisi)            
            
        
    