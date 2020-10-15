import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    c=0
    rem=0
    t=0
    for i in range(n):
        a[i]+=rem
        if a[i]<k:
            print(i+1)
            break
        else:
            rem=a[i]-k
    if rem>k:
        y=rem//k
        print(n+y+1)
        
