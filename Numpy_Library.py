import numpy as n
from time import process_time

li = [temp for temp in range(100000)]
start_time = process_time()
li = [temp+5 for temp in li]
end_time = process_time()
print(end_time-start_time)

np_array = n.array([temp for temp in range(100000)])
start_time = process_time()
np_array  += 5
end_time = process_time()
print(end_time - start_time) 