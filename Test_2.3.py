#Take input from user
age=int(input("Enter a Number "))

#check age group
if(age<5 or age==5):
  print("Too young")
elif(age<12 or age==12):
  print("You're a kid")
else:
  print("Your a Teen or older")