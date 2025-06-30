#Create variables to replace
letter = '''Dear <|NAME|>,
You are selected!
Date: <||DATE>
'''
#Take input from User
Name=str(input("Enter your Name "))
Date=str(input("Enter the current date "))

#Replace the variables
letter = letter.replace("<|NAME|>" ,Name)
letter = letter.replace("<||DATE>", Date)

#print Variables
print(letter)