import numpy as np
import matplotlib.pyplot as plt

a = np.array([0, 1, 2, 3, 4]) #cast list as array

"""
type(a) : numpy.ndarray
a.dtype : dtype('int64')
a.size : 5
a.ndim : 1 number of dimensions
a.shape : (5,) tuple of integers with the size in each dimension
"""

c = np.array([20, 1, 2, 3, 4])
c[0] = 100
d = c[1:4]
c[3:5] = 300, 400

""" Vector addiction and substraction
u = (1, 0)
v = (0, 1)
z = u + v = (1 + 0, 0 + 1)
"""

u = [1, 0]
v = [0, 1]
z = []

for n, m in zip(u, v):
    z.append(n + m)

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v

""" Array multiplication with a scalar
"""
y = np.array([1, 2])
z = 2 * y

""" Product of two numpy arrays
"""
u = np.array([1, 2])
v = np.array([3, 2])
z = u * v

""" Dot product
"""
result = np.dot(u, v)

""" Adding constant to a numpy array
"""
u = np.array([1, 2, 3, -1])
z = u + 1
# z : array([2, 3, 4, 0])

""" Universal functions: mean, maximum value
"""
a = np.array([1, -1, 1, -1])
mean_a = a.mean()
max_a = a.max()

""" Create a numpy array in radians
"""
x = np.array([0, np.pi/2, np.pi])
y = np.sin(x) #apply sin to each component in the vector

np.linspace(-2, 2, num = 5) #-2, -1, 0, 1, 2
np.linspace(-2, 2, num = 9) #-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2


""" Two dimensional Numpy
"""
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
A = np.array(a)

# A.ndim : 2 number of dimensions
# A.shape : (3, 3) number of lists/rows, elements in list/columns
# A.size : 9

# A[0, 0:2] : array([13, 23])

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
Z = X + Y
# Z : array([[3, 1], [1, 3]])

Y = np.array([[2, 1], [1, 2]])
Z = 2 * Y
# Z : array([[4, 2], [2, 4]])

X = np.array([[1, 0], [0, 1]])
Y = np.array([[2, 1], [1, 2]])
Z = X * Y
# Z : array([[2, 0], [0, 2]])

""" Matrix multiplication
"""
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
C = np.dot(A, B)
# C : array([[0, 2], [0, 2]])

