from numpy import linalg as LA
import numpy as np
M1=np.array([[0,1],[5,3]])
M2=np.array([[1,2],[4,3]])

eigenvalue1=list(LA.eig(M1)[0])
eigenvalue2=list(LA.eig(M1)[0])

print(eigenvalue1)
print(eigenvalue2)
print(eigenvalue1==eigenvalue2)

