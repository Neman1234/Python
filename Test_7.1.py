number_1 = float(input("Enter a Number "))
number_2 = float(input("Enter another Number "))
sum = number_1 + number_2
if number_1>number_2:
  diffrence = number_1 - number_2
  print("Diffrence:", diffrence)
else:
  diffrence = number_2 - number_1
  print("Diffrence:",diffrence)
print(f"{sum:.5f}")