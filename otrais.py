a=int(input())
pedcip=a%10
eiro= a//100
cent_atl= a%100
if pedcip ==1:
print(eiro, "eiro",cent_atl, "cents")
else: print(eiro, "eiro", cent_atl, "centi")