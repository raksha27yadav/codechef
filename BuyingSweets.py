for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    sm=sum(a)
    rem=sm//k
    t=0
    if sm%k==0:
        print(rem)
    else:
        for i in range(n):
            b=sm-a[i]
            if b//k==rem:
                print("-1")
                t+=1
                break
        if t==0:
            print(rem)
