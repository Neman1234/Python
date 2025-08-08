#take input from the user
number_1=int(input("Enter a Number with no decimals "))
number_2=int(input("Enter another Number with no decimals "))

#do the math
import math
answer=math.gcd(number_1,number_2)

#print the answer
print(answer)