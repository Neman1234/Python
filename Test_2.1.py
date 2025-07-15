#Take input from user
Number_1=int(input("Enter a Number "))
Number_2=int(input("Enter another Number "))
Number_3=int(input("Enter Another Number "))
Number_4=int(input("Enter Another Number "))

#check the variables
if (Number_1>Number_2):
    f1=Number_1
else:
    f1=Number_2

if(Number_3>Number_4):
  f2=Number_3
else:
   f2=Number_4

#print the number
if(f1>f2):
  print(str(f1) , "is greatest")
else:
   print(str(f2) , "is greatest")