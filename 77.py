n=int(input())
i=1
dic={}
maxn=0

while i <=n:
    s=list(map(int,input().split()))
    dic[chr(i+64)]=s
    i+=1
for p in dic:
    for j in dic[p]:
        if j>maxn:
            maxn=j
            maxk=p
print(maxk,maxn)