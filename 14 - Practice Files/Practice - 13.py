# question1: write a function to print the length of a list of cities | cities = ["geneva", "oslo", "torshavan", "stockholm", "bergen", "reykjavic"]
cities = ["geneva", "oslo", "torshavan", "stockholm", "bergen", "reykjavic"] 
def len_cities(a):
    print(len(a))
    return(len(a))

len_cities("geneva")
len_cities("oslo")
len_cities("torshavan")
len_cities("stockholm")
len_cities("bergen")
len_cities("reykjavic")


# question2: write a function to print the elements of a list in a single line | list = ["python", "power bi", "sql", "excel"]
my_list = ["python", "power bi", "sql", "excel"]
def print_list(a):
    print(*a)

print_list(my_list)


# question3: write a function to find the factorial of n | n = 5 (at first see the actual factorial solution using for loop with comment) 
# n = 5 
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# print(fact)
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(3)
cal_fact(4)
cal_fact(5)


# question4: write a function to convert usd to inr 
def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(1)
converter(10)
converter(100)


# question5: write a function to show ODD if the actual number is odd and show EVEN if the actual number is even
def show(num):
    if num % 2 == 0:
        print("EVEN")
    else:
        print("ODD")

show(13)
show(20)