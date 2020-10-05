from itertools import combinations
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=[]
    res="No"
    for i in range(n):
        l.append(int(input()))
    for i in range(1,n+1):
        temp=list(combinations(l,i))
        for i in temp:
            if sum(i)==m:
                res="Yes"
                break
    print(res)
