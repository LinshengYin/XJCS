a,b,c=map(int,input().split())
aa,bb=int(c/a)+1,int(c/b)+1
f=False
for i in range(0,aa):
    if f==True:
        break
    for j in range(0,bb):
        if i*a+j*b==c:
            print('Yes')
            f=True
            break
if f==False:
    print('No')