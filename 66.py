a=int(input())
b=int(input())
def z(x):
    flag=True
    if x==1: flag=False  
    for q in range(2,int(x**0.5)+1):
        if x%q==0:
            flag= False
            break
    return flag  
for i in range(a,b+1):
    print(i,end=' ') if z(i) else 0