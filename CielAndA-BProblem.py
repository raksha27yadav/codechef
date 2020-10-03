a,b=map(int,input().split())
k=a-b
k=str(k)
ad="1"
if k[0]=="1":
    ad="2"
if len(k)==1:
    print(ad)
else:
    print(ad+k[1:])
