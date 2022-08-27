n=int(input())
m=''
while n>0:
    m=str(n%2)+m
    n=n//2
print(m)