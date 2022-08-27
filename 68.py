m=int(input())
n=m//5
for i in range(0,n+1):
    r=m-i*5
    h=r//3
    for q in range(0,h+1):
        u=m-i*5-q*3
        if i+q+u*3==m:
            print(i,q,u*3)