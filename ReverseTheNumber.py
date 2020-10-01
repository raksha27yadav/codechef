for i in range(int(input())):
    n=input()
    a=n[::-1]
    while a[0]=="0":
        a=a[1:]
    print(a)
