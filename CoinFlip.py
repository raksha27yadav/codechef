for _ in range(int(input())):
    for i in range(int(input())):
        st,en,coin=map(int,input().split())
        if en%2==0:
            print(en//2)
        else:
            if st==coin:
                print(en//2)
            else:
                print(en//2+1)
    
