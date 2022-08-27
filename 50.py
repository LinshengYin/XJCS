a=float(input())
d=b=0.005
c=1
while d<a:
    c+=1
    d=b*(2**c)
print(c)