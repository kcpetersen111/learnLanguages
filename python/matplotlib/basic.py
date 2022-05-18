import matplotlib.pyplot as plt

import numpy as np

# the plot and show are commented out so only one plot is shown to reduce confusion and improve runtime speed
x = np.array([1,2,3])
y = np.array([3,2,1])

# plt.plot(x,y)
# plt.show()

#can just pass one array to the plot function
y= np.random.normal(size=100)

# plt.plot(y)
# plt.show()

#can modify the plot with more options

x = np.random.random(size=100)
y = np.random.random(size=100)
x*=10
y*=5
#plt will plot only dots

# plt.plot(x,y, 'o')
# plt.show()

#plt will put dots (marker) on the points, make the color blue, and make the line with dots and dashes

# plt.plot(x,y, marker='D', color='b', linestyle='-.')
# plt.show()

y = np.arange(10,0,-1)


#can shorten the code  by using a single string with back to back characters

# plt.plot(y, 'o:r')
# plt.show()

#can change the color of the marker face

# plt.plot(y, 'o-r', mfc='b', mec='b')
# plt.show()

#can use hex colors 

# plt.plot(y, 'o-r', mfc='#0f0f0f', mec='#0f0f0f')
# plt.show()

#can use multiple lines
x = np.arange(10)

# plt.plot(x, 'o-r')
# plt.plot(y, 'o-b')
# plt.show()

#there are additional decoration options for lines and markers

#can add labels to the axes

# plt.plot(y)
# plt.xlabel('The x axis')
# plt.ylabel('The y axis')
# plt.title('The title')
# plt.show()

# the labels also have a great amount of customization options

#can enable grid lines

# plt.plot(y)
# plt.grid()
# plt.show()

#can change it so that the grid lines are only on one axis

# plt.plot(y,'D-.g')
# plt.grid(axis='y')
# plt.show()

#can change the grid to have different color, line style, and line width
plt.plot(y)
plt.grid(color='r', linestyle='--', linewidth=2)
plt.show()  