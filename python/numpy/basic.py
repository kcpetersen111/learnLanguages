import numpy as np

#basic array
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# zero d array 
arr = np.array(5)
print(arr)

#3d array
arr = np.array([[[1],[2],[3]],  [[4],[5],[6]], [[7],[8],[9]]])
print(arr)

#check number of dimensions
print(arr.ndim)

# n dimensional array
arr = np.array([1,2,3,4,5], ndmin= 5)
print(arr)

#access array 
arr = np.array([[1,2,3],[4,5,6]])
print(arr[0,1])


#slicing works just like it does with normal arrays
print(arr.dtype)

arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
arr = arr.astype(int)
print(arr)

arr = np.array([1,0,3])
arr = arr.astype(bool)
print(arr)


#copy will actual copy the array and not just reference the same array
#view will just reference the same array

arr = np.array([1,2,3], ndmin=3)
print(arr)
print(arr.shape)

print()

arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
arr = arr.reshape(2,5)
print(arr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = arr.reshape(2,3,-1)
print(arr)
print(arr.reshape(-1))

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = arr.reshape(2,3,-1)
for x in arr:
    print(x)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['d']):
    print(x)

arr1 = np.array(["1","2","3"])
arr2 = np.array(["4","5","6"])
print(np.concatenate([arr1, arr2]))


arr1 = np.array([["1","2","3"],["10","20","30"]])
arr2 = np.array([["4","5","6"],["7","8","9"]])
print(np.concatenate([arr1, arr2], axis=1))

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
arr = np.concatenate([arr1, arr2], axis=0)
print(arr)

print()

#vstack is vertical stack and hstack is horizontal stack and dstack is along height
print(np.vstack((arr1,arr2)))
print(np.hstack((arr1,arr2)))   
print(np.dstack((arr1,arr2)))


print()

arr = np.array([1,2,3,4,5,6])
arr2 = np.array_split(arr, 2)
arr = np.array((arr2[0],arr2[1]))
print(arr)

#there is a vsplit, hsplit and dsplit



print()

#search using the where command
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 1)
print(x)

#sorting
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

#can filter arrays by accessing the array at the index of a mask that you pass in