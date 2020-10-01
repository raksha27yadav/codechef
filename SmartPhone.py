a=[]
for i in range(int(input())):
    a.append(int(input()))
a.sort(reverse=True)
c=0
for i in range(len(a)):
    l=(i+1)*a[i]
    c=max(c,l)
print(c)
    
