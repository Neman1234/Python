#Take input from User
sub1=int(input("Enter a Number "))
sub2=int(input("Enter another Number "))
sub3=int(input("Enter another Number "))

#check the marks
if(sub1<33 and sub2<33):
    print("You are fail because you have less then 33% in one of the subjects ")
elif(sub1+sub2+sub3)/3<40:
    print("You fail due to your total percentage less then 40")
else:
    print("Congatulations! you passed the exam")