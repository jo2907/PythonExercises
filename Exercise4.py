import numpy as np 
r = np.array(np.random.randint(1,10,20))

idx = r<5
print(r)
print(idx)
# sets all cases where this is true to 0 
r[idx] = 0
print(r)