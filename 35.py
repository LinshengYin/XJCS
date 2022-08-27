a=int(input())
b=int(input())
c=str(input())
if c=="+" or c=="-" or c=="*" or c=="/":
    if c=="+":
        print(a+b)
    elif c=="-":
        print(a-b)
    elif c=="*":
        print(a*b)
    else :
        if b==0:
            print("Divided by zero!")
        else:
            print(int(a/b))

else:
    print("Invalid operator!")