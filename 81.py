k=list(map(int,input().split()))
pingwei=k[0]
zuopin=k[1]
s=[[0 for i in range(zuopin)]for j in range(pingwei)]
for n in range(pingwei):
    s[n]=list(map(int,input().split()))
for k in range(zuopin):
    max=s[0][k]
    min=s[0][k]
    maxp2=0
    minp2=0
    pingjun0=0
    for i in range(pingwei):
        pingjun0+=int(s[i][k])
        if s[i][k]>=max:
            max= s[i][k]
            maxp2=i
        elif s[i][k]<=min:
            min= s[i][k]
            minp2=i
    pingjun=int((pingjun0-s[maxp2][k]-s[minp2][k])/(pingwei-2))
    print(k+1,pingjun)