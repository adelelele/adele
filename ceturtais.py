n=(int(input()))
a=(int(input()))
k=(int(input()))
if n>=a:
    apavusk= n%a
    kreklusk= n%k
if apavusk == kreklusk:
    print(apavusk, kreklusk, "Apavi", "Krekli")
else if apavusk > kreklusk:
    print(apavusk, kreklusk, "Apavi")
else: print(apavusk, kreklusk, "Krekli")
    