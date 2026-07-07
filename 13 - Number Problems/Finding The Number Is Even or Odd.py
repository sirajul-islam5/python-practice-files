# write a program if a number entered by the user is odd or even 

num = int(input("enter number: "))

rem = num % 2 

if (rem == 0):
    print("even")
else:
    print("odd")