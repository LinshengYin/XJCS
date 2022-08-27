n=int(input())
b=1
m=1+(n-1)*2
for a in range(1,n+1):
    c=int((m-b)/2)
    print(c*" "+b*"*")
    b+=2