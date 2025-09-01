import numpy as np
from time import process_time

li = [temp for temp in range(100000)]
start_time = process_time()
li = [temp+5 for temp in li]
end_time = process_time()
print(end_time-start_time)

np_array = np.array([temp for temp in range(100000)])
start_time = process_time()
np_array  += 5
end_time = process_time()
print(end_time - start_time) 

np_array = np.array([1,2,3,4,5])
print(np_array)
type(np_array)

li = [1,2,3,4,5]
print(li)
type(li)

np_array = np.array([1,2,3,4,5,6,7])
print(np_array)
print(np_array.shape)
print(type(np_array))

b= np.array([(1,2,3,4),(5,6,7,6),(8,9,10,11)])
print(b)


c= np.array(([(1,2,3,4),(5,6,7,8)]), dtype=float)
print(c.shape)

d= np.zeros((10))
print(d)
e= np.zeros((10,5))
print(e)

f= np.array(([(1,2,3,4),(5,6,7,8)]), dtype=float)
print(c.shape)

g= np.ones((10))
print(g)
e= np.ones((10,5))
print(e)

h= np.full((4,5),500000000)
print(h)


i= np.eye(5)
print(i)

z= np.random.random((3,4))
print(z)

a1= np.random.randint(1,4,(6,5))
print(a1)