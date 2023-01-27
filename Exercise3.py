import numpy as np

a = np.array([5,4,9,2,0,4,7,-9])
print(a[-1])
#prints second to fifth element
print(a[1:6])
#prints first to third-to-last elemeny
print(a[:-2])
#prints every other element starting at first
print(a[::2])
# change the first three elemenys of a to 1
a[0:3] = 1
print(a)