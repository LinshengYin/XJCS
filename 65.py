n=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
m=1
for i in l:
    m*=i
for i in range(l[0],m+1,l[0]):
    r=True
    for j in range(1,n):
        if i%l[j]!=0:
            r=False
            break
    if r==True:
        print(i)
        break