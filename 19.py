a=int(input())
b=int(input())
c=int(input())
if a+b>c and a+c>b and b+c>a and a-b<c and a-c<b and b-c<a:
    p=1/2*(a+b+c)
    s=round((p*(p-a)*(p-b)*(p-c))**0.5,2)
    if int(s) == float(s):
        print(str(s)+"0")
    else:
        print(round(s,2))
else:
    print("It is not a triangle.")