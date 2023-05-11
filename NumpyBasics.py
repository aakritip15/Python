import numpy as np 
import matplotlib.pyplot as plt
a = np.array([0, 1, 2, 3, 4])

print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])
print(type(a))
print(a.dtype)
# Changing new value
a[1]=20
print(a)

# Slicing
d = a[1:4]
print(d)
# Assigning new values 
a[3:5] = 300, 400
print(a)

#Print the even elements in the given array. [start:end:step]
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
arr[1:8:2]


# Attributes
b = np.array([10, 20, 30, 40, 50, 60, 70])
b.size
b.ndim
b.shape


# Statistical Function
a = np.array([1, -1, 1, -1])
mean = a.mean()
max_b = b.max()
min_b = b.min()
type(min_b)
standard_deviation=a.std()

# Array Operations
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3 = np.add(arr1, arr2)
arr3 = np.dot(arr1, arr2)
arr3 = np.multiply(arr1, arr2)

#Sine Curve 

x = np.linspace(0, 2*np.pi, num=100)
y = np.sin(x)
# plt.plot(x, y)


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

u = np.array([1, 0])
v = np.array([0, 1])
z = np.add(u, v)
Plotvec1(u,z,v)
