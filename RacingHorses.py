for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    k=100000000000000000
    for i in range(n-1):
        diff=a[i+1]-a[i]
        k=min(k,diff)
    print(k)
