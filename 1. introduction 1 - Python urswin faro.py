# Question 1: Variable Assignment and String Manipulation

# TODO: Ask the user for their name and store it in a variable
print("Hello, what is your name?")
username = input ("name: ")
# TODO: Ask the user for their age and store it in a variable
print("How old are you?")
userage = input("age: ")
# TODO: Print a greeting using the name and age variables
print("Hi " + username + " age " + userage + ", glad you joined the team! ")
#------------------------------------------------------------------------------------
# Question 2: Integer Operations

# TODO: Ask the user for the length of a rectangle and store it as an integer
print(username + " What is the leangth of the rectangle?")
x = int(input("length: "))
# TODO: Ask the user for the width of a rectangle and store it as an integer
print("What is the width of the rectangle?")
y =int(input("width: "))
# TODO: Calculate the area of the rectangle
sum = x * y
# TODO: Print the result
print(sum)
#------------------------------------------------------------------------------------
# Question 3: Working with Floats

# TODO: Ask the user for a temperature in Celsius and store it as a float
print("What is the temperature in calsius?")
temp = float(input("temp: "))
letter = '°F'
# TODO: Convert the temperature to Fahrenheit using the formula: (C * 9/5) + 32
sum = (temp * 9/5) + 32
# TODO: Print the result rounded to two decimal places
round_number = str(round(sum , 2)) + letter
print(round_number) 