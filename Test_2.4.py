#Take input from user
Marks=float(input("Enter a Grade with decimals "))

#Check the Grade
if (Marks>90 or Marks==90):
    print("A+")
elif(Marks>80 or Marks==80):
    print("A")
elif(Marks>70 or Marks==70):
    print("B")
else:
    print("Keep Trying")