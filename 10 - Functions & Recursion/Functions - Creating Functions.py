# functions used for decressing redundancy 
# function definition: 

# uses1:
def calc_sum(a, b): # parameters = a,b
    sum = a + b
    print(sum)
    return sum 

calc_sum(5, 10) # function call | arguments = 5,10 

# more lines of code

calc_sum(2, 10)

# more lines of code

calc_sum(12, 17)


# uses2: 
def print_hello():
    print("hello")

print_hello()
print_hello()


# uses3: average of 3 numbers
def avg_num(a, b, c):
    avg = (a + b + c)/3
    print(avg)
    return avg

avg_num(2, 3, 4)
avg_num(10, 15, 20)