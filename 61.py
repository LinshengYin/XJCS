a=input()
list=[a.find('C'),a.find('H'),a.find('O')]
l=[]
for i in range(2):
    if list[i+1]-list[i]>1:
        l.append(int(a[list[i]+1:list[i+1]]))
    else: 
        l.append(1)
if list[2]+1<len(a):
    l.append(int(a[list[2]+1:]))
else:
    l.append(1)
print(l[0]*12+l[1]+l[2]*16)