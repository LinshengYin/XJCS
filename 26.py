m,n=map(int,input().split())
ml,nl=m,n
mn,nn=0,0
k=int(input())
while k>0:
    if ml>0 and nl>0:
        print(mn+1,nn+1)
        ml-=1
        nl-=1
        mn+=1
        nn+=1
        if ml==0:
            ml=m
            mn=0
        if nl==0:
            nl=n
            nn=0
    k-=1