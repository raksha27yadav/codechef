for _ in range(int(input())):
    activity=input().split()
    h={"TOP_CONTRIBUTOR":300,"CONTEST_HOSTED":50}
    total=0
    for i in range(int(activity[0])):
        st=input().split()
        if len(st)==2:
            if st[0]=="BUG_FOUND":
                    total+=int(st[1])
            else:
                if int(st[1])<=20:
                    total+=320-int(st[1])
                else:
                    total+=300
        else:
            total+=h[st[0]]
    if activity[1]=="INDIAN":
        print(total//200)
    else:
        print(total//400)
