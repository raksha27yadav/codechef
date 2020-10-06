for _ in range(int(input())):
    start,end=map(int,input().split())
    s=set()
    for i in range(2,int(end**0.5)+1):
      for j in range(max(start//i,2),(end//i)+1):
        s.add(i*j)
    for k in range(max(start,2),end+1):
        if k not in s:
          print(k)
