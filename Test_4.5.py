num=int(input("Enter a Number with No Decimals "))
factorial=1
temp=1

while temp<=num:
    factorial *=temp
    temp +=1

print(f"The factorial of {num} is {factorial}")