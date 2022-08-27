l=list(map(int,input().split(",")))
n=int(input())
k=0
for i in range(len(l)-1):
    k=k+l[i]*n**(len(l)-i-1)
k+=l[len(l)-1]
print(k)