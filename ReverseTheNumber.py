def call(a,b):
    h={}
    for i in a:
        if i in h:
            h[i]+=1
        else:
            h[i]=1
    for i in b:
        if i in h:
            h[i]-=1
        else:
            h[i]=1
    for i in h:
        if h[i]!=0:
            return False
    return True
for i in range(int(input())):
    n=input()
    k=len(n)//2
    if len(n)%2==0:
        if call(n[:k],n[k:]):
            print("YES")
        else:
            print("NO")
    else:
        if call(n[:k],n[k+1:]):
            print("YES")
        else:
            print("NO")

