#initial sequence
L=[0,1]

for i in range(18):
    #sum of the last 2
    a=L[-1]+L[-2]
    L.append(a)
print(L)
#ratio
R=[]
for i in range(len(L)-1):
    r=L[i]/L[i+1]
    R.append(r)
print(R)

