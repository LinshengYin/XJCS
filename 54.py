a=int(input())
b=int(input())
c=0
if  a%2==1:
    if b%2==0:
        for d in range(a+1,b+1,2):
            c+=d
    if b%2==1:
        for d in range(a+1,b,2):
            c+=d
else:
    if b%2==0:
        for d in range(a,b+1,2):
            c+=d
    if b%2==1:
        for d in range(a,b,2):
            c+=d
    
print(c)