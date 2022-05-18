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

# plt.plot(y)
# plt.grid(color='r', linestyle='--', linewidth=2)
# plt.show()  

#can show multiple plots on the same figure
# in the subplot command it takes 3 arguments: the number of rows, the number of columns, and the number of the plot

# #plot 1
# plt.subplot(1,2,1)
# plt.plot(x)
# #plot 2
# plt.subplot(1,2,2)
# plt.plot(y)
# plt.show()

# here is an example of 4 graphs with some titles and a main title

# #plot 1
# plt.subplot(2,2,1)
# plt.plot(x)
# plt.title('Plot 1')
# #plot 2
# plt.subplot(2,2,2)
# plt.plot(y)
# #plot 3
# plt.subplot(2,2,3)
# plt.plot(y)
# #plot 4
# plt.subplot(2,2,4)
# plt.plot(x)
# plt.title('Plot 4')
# plt.suptitle('The title')
# plt.show()

#can do other types of plots

#a scatter plot requires two arrays of the same size

# plt.scatter(x,y)
# plt.show()

#can do two scatter plots on top of each other

# plt.scatter(x,y, color='r')
# plt.scatter(x,x, color='b')
# plt.show()

#you can color each individual point

# cmap is built in color maps

colorarr = np.arange(0,100,10)
# plt.scatter(x,y, c=colorarr, cmap='RdBu')
# plt.show()

# can also change the size of each point

#can change the transparency with alpha values

sizearr = np.arange(0,100,10)
# plt.scatter(x,y, s=sizearr, cmap='RdBu', c=colorarr, alpha=0.5)
# plt.show()



#can do bar graphs

# plt.bar(x,y)
# plt.show()

#can do horizontal bar graphs

# plt.barh(x,y)
# plt.show()

#can do width(height for horizontal bar graphs) and color

# plt.bar(x,x , width=0.5, color='r')
# plt.show()

#can also do histograms

# plt.hist(x)
# plt.show()

#can pick how many bins to put the data in 

normal = np.random.normal(size=100)
# plt.hist(normal,bins=6)
# plt.show()

#can do pie charts

#can have labels but must have one label for each piece of data

# plt.pie(x, labels=x)
# plt.show()

#can make a piece of data stand out with the explode option

explode = np.array([0,0,0,0,0.2,0,0,0,0,0])
# plt.pie(x, labels=x, explode=explode)
# plt.show()

#can make a pie chart with a legend

plt.pie(x, explode=explode)
plt.legend(x, title='Legend')
plt.show()

