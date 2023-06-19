f=open("FinalGrade")
N=0
P=0
for line in f:
    N=N+1
    line=line.replace("\n","")
    line=line.split(" ")
    grade=float(line[1])
    if grade > 40:
        P=P+1
R=round(100*P/N)
print("Pass rate is "+str(R)+"%")

