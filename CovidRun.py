for i in range(int(input())):
    n,k,x,y=map(int,input().split())
    t=[]
    while x not in t:
        t.append(x)
        x=(k+x)%n 
    if y in t:
        print("YES")
    else:
        print("NO")
