n=int(input())
l=[0]*2+[1]*(n-1)
for i in range(2,n+1):
    if l[i]==1:
        print(i,end=' ')
        for j in range(2*i,n+1,i):
                l[j]=0