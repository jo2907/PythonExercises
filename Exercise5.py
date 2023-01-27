import numpy as np 
A = np.array([[1,0,0,0],[1,-2,1,0],[0,1,-2,1],[0,0,0,1]])
b = np.array([0,1,1,2])
x = np.linalg.solve(A,b)
print(x)

print(np.matmul(A,x) - b)