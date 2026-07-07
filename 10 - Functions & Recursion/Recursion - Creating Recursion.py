# recursive function 
def show(n):
    if n == 0:  # base case
        return
    print(n)
    show(n-1)
    print("end")

show(3)

# recurrence relation | 5! = 4!x5  | 4! = 3!x4 | n! = (n-1)!xn 
def fact(n): 
    if(n == 0 or n == 1):
        return 1
    return fact(n-1) * n

print(fact(2))
print(fact(3))
print(fact(4))