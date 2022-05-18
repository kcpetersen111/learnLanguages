from scipy import constants as sciC
from scipy import optimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from scipy.spatial import Delaunay
from scipy.spatial import ConvexHull
from scipy.interpolate import interp1d
from scipy.stats import describe
from scipy.stats import normaltest
import matplotlib.pyplot as plt
# import scipy
from math import cos
import numpy as np

print(sciC.pi)

for const in dir(sciC):
    print(const)    # list of all constants
print()

print(sciC.kilo)    # kilo will return 1000 because it is a thousand meters

# also has constants for bianary, mass, angle, time, length, pressure, 
# area, volume, speed, temperature, energy, power, force

# uses the metric system

#can find the root of an equation
def eqn(x):
  return x + cos(x)
myroot = optimize.root(eqn, 0)
print(myroot)


print()

def diverge(x):
    return (-1)**x  
    # return x**2
mydiv = optimize.root(diverge, 0)
print(mydiv)

# can also find the minimum of an equation


print()

def eqn2(x):
    return x**2 - 4
mymin = optimize.minimize(eqn2, 0)
print(mymin)


#working with sparse data

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])
print(csr_matrix(arr))
print()

arr = np.array([[0, 0, 0, 0],[ 1, 1, 0, 2]])
print(csr_matrix(arr))
print()

#does not work sparce only works with 1 or 2 dimensional arrays
arr = np.array([[[0, 0, 0, 0],[ 1, 1, 0, 2]],[[0, 0, 0, 0],[ 1, 1, 0, 2]]])
# print(sparse.csr_matrix(arr))

print()
arr = np.array([[0, 0, 0, 0],[ 1, 1, 0, 2]])
print(csr_matrix(arr).data)
print()

arr = np.array([[0, 0, 0, 0],[ 1, 1, 0, 2]])
print(csr_matrix(arr).count_nonzero())
print()
print()
print()
#will return output a description of the matrix
arr = np.array([[0, 0, 0, 0],[ 1, 1, 0, 2]])
arr  = (csr_matrix(arr))
arr.eliminate_zeros()
print(arr.data)
print()


arr = np.array([[0, 0, 0, 0],[ 1, 1, 0, 2]])
arr  = csr_matrix(arr)
# arr.sum_duplicates()
arr = arr.tocsc()
print(arr)
print()


arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])
newarr = csr_matrix(arr)
print(connected_components(newarr))

#can do built in search algos in the matrix 

#can find the area of a shape with triangulation
# just so multiple matplots do not show up
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1]
])
simplices = Delaunay(points).simplices
# plt.triplot(points[:, 0], points[:, 1], simplices)
# plt.scatter(points[:, 0], points[:, 1], color='r')

# plt.show()


#the convex hull is the smallest convex polygon that contains all the points
points = np.array([
  [2, 4],
  [3, 4],
  [3, 0],
  [2, 2],
  [4, 1],
  [1, 2],
  [5, 0],
  [3, 1],
  [1, 2],
  [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:,0], points[:,1])
for simplex in hull_points:
  plt.plot(points[simplex,0], points[simplex,1], 'k-')

# plt.show()

#can do stuff like import and export data to matlab format


#can interpolate data 

xs = np.arange(10)
ys = 2*xs + 1

interp_func = interp1d(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)

#can do a lot about all stats in scipy

norm = np.random.normal(size=100)
print(describe(norm))

print()
print(normaltest(norm))