for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    chef=[]
    assi=[]
    fin=[]
    for i in range(1,n+1):
       if i not in a:
           fin.append(i)
    for i in range(len(fin)):
        if i%2==0:
            chef.append(fin[i])
        else:
            assi.append(fin[i])
    print(*chef)
    print(*assi)
