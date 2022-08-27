sum=100000000
b=0.2
k=int(input())
g=0
while sum>0:
    sum-=b
    g+=1
    b*=k
print(g)