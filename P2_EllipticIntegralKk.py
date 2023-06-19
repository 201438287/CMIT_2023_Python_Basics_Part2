import numpy as np
import math
#Trapezium
def K_integrand(k,theta):
    d=1-k**2*(math.sin(theta))**2
    y=1/(math.pow(d,1/2))
    return y
X=np.linspace(0,0.999, num=500)
Y=[]

for x in X:
    T=np.linspace(0,np.pi/2, num=500)
    dt=T[1]-T[0]
    Klocal=[]
    for t in T:
        Klocal.append(K_integrand(x,t))
    I=sum(Klocal)*dt-(T[0]+T[1])/2
    Y.append(I)

f=open("EllipticIntegralKk","w")
for i in range(len(X)):
    x=str(X[i])
    y=str(Y[i])
    f.write(x+" "+y+"\n")
f.close()

'''
T=np.linspace(0,np.pi/2, num=500)
#increment in theta
dt=T[1]-T[0]
K=[]
for t in T:
    K.append(Khalf(t))
#integral 
I=sum(K)*dt-(T[0]+T[1])/2
print(I)
'''

