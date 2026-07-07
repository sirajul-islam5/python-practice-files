# question1: write a program to find the sum of first n numbers (using for)
n = 5 
sum = 0 
for i in range(1, n+1):
    sum += i
print("total sum = ", sum) # outside only print once 


# question2: write a program to find the sum of first n numbers (using while) 
n = 5 
sum = 0 
i = 1
while i <= n:
    sum += i
    i += 1 
print("total sum =", sum)


# question3: write a program to find the factorial of first n numbers (using for)
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("factorial =", fact)


# question4: write a program to find the factorial of first n numbers (using while)
n = 5
fact = 1 
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)
