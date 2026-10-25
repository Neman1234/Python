import time
 
#print("Ready...")
#time.sleep(60)
#print("Go!")

start = time.perf_counter()
 
total = 0
for number in range(1_000_000):
    total += number
 
finish = time.perf_counter()
 
print("Total:", total)
print("Seconds:", finish - start)