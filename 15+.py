s,n=0,0
a,b=map(int,input().split())
while a!=b:
    if 8<=a<19:
        s+=12
    else:
        n+=4
    a+=1
    a%=24
n=min(10,n)
print(min(s+n,96))