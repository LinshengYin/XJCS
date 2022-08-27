a,b=map(int,input().split())
maxn=10
max=96
sum1=0
sum2=0
sum3=0
sum=0

if a>=8 and a<19:
    if b>a:
        if b<=19:
            sum=(b-a)*12
        else:
            sum1=(19-a)*12
            sum2=(b-19)*4
            if sum2>maxn:
                sum2=maxn
    else:
        sum1=(19-a)*12
        sum2=maxn
        if b>8:
            sum3=(b-8)*12
elif a<8:
    if b>a:
        if b<=8:
            sum=(b-a)*4
            if sum>maxn:
                sum=maxn
        elif b>8 and b<=19:
            sum1=(8-a)*4
            if sum1>maxn:
                sum1=maxn
            sum2=(b-8)*12
        else:
            sum=max
    else:
        sum=max
else:
    if b>a:
        sum=(b-a)*4
        if sum>maxn:
            sum=maxn
    else:
        if b<=8:
            sum=(24-a+b)*4
            if sum>maxn:
                sum=maxn
        elif b>8 and b<=19:
            sum1=maxn
            sum2=(b-8)*12
        else:
            sum=max

if sum1+sum2+sum3>max:
    sum=max
elif sum==0:
    sum=sum1+sum2+sum3
print(sum)