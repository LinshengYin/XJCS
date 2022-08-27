for i in range(1,10):
    for j in range(1,i+1):
        a= i*j
        if a < 10:
            a = " "+str(a)
        if j == i:
            print(str(j)+"*"+str(i)+"="+str(a))
        else:
            print(str(j)+"*"+str(i)+"="+str(a),end=" ")