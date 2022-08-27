num=str(input())
k=0
for i in range(len(num)):
    if ord(num[i]) < ord("0") or ord(num[i]) > ord("9"):
        k=0
        break
    if num[i] != num[len(num)-i-1]:
        k=0
        break
    
    k+=1
if k!=0:
    print("True")
else:
    print("False")