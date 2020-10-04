for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    k=int(input())
    johny=a[k-1]
    a.sort()
    print(a.index(johny)+1)
