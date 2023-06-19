import matplotlib.pyplot as plt
f=open("EllipticIntegralKk","r")
X=[]
Y=[]
for line in f:
    line=line.replace("\n","")
    line=line.split(" ")
    X.append(float(line[0]))
    Y.append(float(line[1]))
f.close()
plt.plot(X,Y)
plt.savefig("EllipticIntegralPlot.eps")
plt.show()
plt.close()

