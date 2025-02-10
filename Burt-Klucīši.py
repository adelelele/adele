vards=input()
iedomvards=input()
sakritiba=0
for p in range (len(vards)):
    for o in range (len(iedomvards)):
        if vards[p]==iedomvards[o]:
            sakritiba+=1
            iedomvards=iedomvards[:o]+'#'+iedomvards[o+1:]
            break
if sakritiba == len(iedomvards):
    print("VAR")
else:
    print("NEVAR")