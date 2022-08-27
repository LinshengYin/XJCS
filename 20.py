sum,sco=map(float,input().split(","))
sco=int(sco)
bill=round(float(sum),2)
if sco>=8000:
    bill=round(sum*0.6,2)
elif sco>=6000:
    bill=round(sum*0.7,2)
elif sco>=4000:
    bill=round(sum*0.8,2)
elif sco>=2000:
    bill=round(sum*0.9,2)
if int(bill)==bill:
    print(str(bill)+"0")
elif round(round(bill%1*10,2)%1,2)==0:
    print(str(bill)+"0")
else:
    print(bill)