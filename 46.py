num=input()
n=int(input())
k=0
for i in range(len(num)-1):
    if num[i]>="0"and num[i]<="9":
        k=k+int(num[i])*n**(len(num)-i-1)
    elif num[i]>="A" and num[i]<="F":
        k=k+int((ord(num[i])-ord("A")+10))*n**(len(num)-i-1)
if num[len(num)-1]>="0"and num[len(num)-1]<="9":
    k+=int(num[len(num)-1])
else:
    k+=int((ord(num[len(num)-1])-ord("A")+10))
print(k)