# question1: print numbers from 1 to 100
i = 1 
while i <= 100: # stopping condition
    print(i)
    i += 1
print("loop ended")


# question2: print numbers from 100 to 1 
i = 100
while i >= 1: # stopping condition
    print(i)
    i -= 1
print("loop ended")


# question3: print the multiplication table of a number n
i = 1 
n = int(input("enter the number: "))
while i <= 10:
    print(n*i)
    i += 1
print("loop ended")
