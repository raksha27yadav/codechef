a,n,k=map(int,input().split())
b=[0]*k
c=n+1
for i in range(k):
    print(a%c,end=" ")
    a=a//c
  
