import numpy as np
x = np.array(12)
y = np.array([1, 2, 3, 4, 5])
z = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
w = np.array([[[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[4, 5, 6], [5, 6, 7], [6, 7, 8]], [[7, 8, 9], [8, 9, 10], [9, 10, 11]]])
print(x)
print(x.ndim)
print(y)
print(y.ndim)
print(z)
print(z.ndim)
print(w)
print(w.ndim)