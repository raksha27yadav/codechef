for _ in range(int(input())):
    n=int(input())
    count=n//5
    res=n//5
    while count/5>0:
        count=count//5
        res+=count
    print(res)
