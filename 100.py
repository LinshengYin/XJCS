st=input()
word=input()
len0=len(word)
re=''
q=0
def des(a,st,len0,word):
    if st[a:a+len0]==word and st[a-1]==' ' and st[a+len0]==' ':
        return True
    else:
        return False
for i in range(len(st)-len0):
    if des(i,st,len0,word):
        st=st[:i]+st[i+len0+1:]
        re=re+str(i+q)+' '
        q+=len0+1
if re=='':
    print(st)
    print('未出现！')
else:
    print(st)
    print(re)