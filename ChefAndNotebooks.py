for _ in range(int(input())):
    x,y,k,n=map(int,input().split())
    c=[]
    rem=x-y
    for i in range(n):
        p,price=map(int,input().split())
        if rem<=p:
            c.append(price)
    if len(c)>0:
        check=min(c)
        if check<=k:
            print("LuckyChef")
        else:
            print("UnluckyChef")
    else:
        print("UnluckyChef")
        
        
