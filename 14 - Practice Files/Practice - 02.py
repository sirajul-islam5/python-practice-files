#question-1: write a program to input 2 interer numbers , a and b. print true if a is greater than or equal to b. if not print false.
a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
if a >= b:
    print("true")
else:
    print("false")


#question-2: write a program to input 3 numbers and print the greatest number among them.
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))  
num3 = int(input("enter the third number: "))
if num1 >= num2 and num1 >= num3:
    print("the greatest number is: ", num1)
elif num2 >= num1 and num2 >= num3:
    print("the greatest number is: ", num2)
else:
    print("the greatest number is: ", num3)    