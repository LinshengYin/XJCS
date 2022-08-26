d=input()
l=[]
for i in range(len(d)):
    for j in range(i,len(d)):
        l.append(d[i:j+1])
for q in l:
    print(q,end=' ')
print()
print(len(l)+1)