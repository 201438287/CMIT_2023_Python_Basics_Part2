#quiz contributes 10%
#exam contributes 90%

#analyse: in the GradeBook,
#the 1st line should not be involved in calculation
f=open("GradeBook","r")
Alpha=list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY")
Students=[]
FinalGrade=[]
for line in f:
    #we do not want the line break in the end of
    #each line
    line=line.replace("\n","")
    #split string line into lists
    #with respect to ,
    line=line.split(",")
    #time for checking
    print(line[1][0])
    if line[1][0] in Alpha:
        
        #if the grade starts with letters, drop it
        continue
        #go to next "line" in the for loop
    Students.append(line[0])
    q=int(line[1])*0.1
    e=int(line[2])*0.9
    final=str(q+e)
    FinalGrade.append(final)
f.close()

N=len(Students)
#let's write now
w=open("FinalGrade","w")
for n in range(N):
    w.write(Students[n]+" "+FinalGrade[n]+"\n")
w.close()



