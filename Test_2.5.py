#Take input from user
Temperature=float(input("Enter a Number for the temperature "))

#check the tempreture
if(Temperature>30 or Temperature==30):
    print("it's hot")
elif(Temperature>20 or Temperature==20):
    print("Nice Weather")
else:
    print("It's Cold")