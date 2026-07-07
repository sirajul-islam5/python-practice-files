# answer the questions using for & range()

# question1: print numbers from 1 to 100
for i in range(1, 101, 1):
    print(i)


# question2: print numbers from 100 to 1
for i in range(100, 0, -1):
    print(i)


# question3: print the multiplication table of a number n 
n = int(input("enter the number:" ))
for i in range(1, 11):
    print(n * i)