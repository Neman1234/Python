#create lists
numbers=[5,4,3,2,1]
negitave_numbers=[-1,-2,-3,-4,-5]

#sort list
numbers.sort()

#print the list
print(numbers)

#reverse the list
negitave_numbers.reverse()

#print the list [2]
print(negitave_numbers)

#insert number into list
numbers.insert(6,0)
numbers.sort()

#print the updated list
print(numbers)

#add a number to the list
numbers.append(6)

#print the updated list [2]
print(numbers)

#pop a item from the list
numbers.pop(0)

#print the updated list [3]
print(numbers)

#remove a item from the list
numbers.remove(6)

#print the updated list [4]
print(numbers)