n=int(input())
dic={}
for i in range(0,n):
    lst1=list(map(int,input().split()))
    dic[i]=lst1
for n in range(0,n):
    for h in range(0,len(dic[n])):
        if h == len(dic[n])-1:
            print(dic[n][h])
        else:
            print(dic[n][h],end=" ")