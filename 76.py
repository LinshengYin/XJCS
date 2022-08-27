n=int(input())
dic={}
li=[]
li2=[]
for i in range(n):
    cla=chr(ord("A")+i)
    dic[cla]=list(map(int,input().split()))
lev=int(input())
for h in dic:
    b=0
    zong=0
    for z in dic[h]:
        if z >=lev:
            b+=1
        zong+=z
    li+=[float(b)/len(dic[h])]
    li2+=[round(zong/len(dic[h]),2)]
for m in range(n):
    c=str(round(li[m]*100,2))+"%"
    print(chr(ord("A")+m),li2[m],c)