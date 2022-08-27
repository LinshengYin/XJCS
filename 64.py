n=int(input())
l=list(map(int,input().split(' ')))
l.sort()
z=[]
for i in range(1,int(l[0]**0.5)+1):
    if l[0]%i==0:
        z.append(i)
        z.append(int(l[0]/i))
z.sort(reverse=True)
m=z[0]
for j in range(1,n):
    if l[j]%m>0:
        for i in z:
            if l[j]%i==0:
                m=i
                break
print(m)