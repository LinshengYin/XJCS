a,b = map(int,input().split())
c=a
while c <= b:
    a+=1
    c+=a
print(c-a,a-1)