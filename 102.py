data=input()
list=[]
for i in range(len(data)):
    for j in range(i,len(data)):
        list.append(data[i:j+1])
for q in list:
    print(q,end=' ')
print()
print(len(list)+1)
