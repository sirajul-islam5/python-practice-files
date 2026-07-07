# structure of range = range(start?, stop, step?)

# uses of range function with specify 
seq = range(5)
for i in seq:
    print(i)


# range with (stop)
for i in range(5):  # range(stop)
    print(i)


# range with (start, stop)
for i in range(2,5):   # range(start, stop)
    print(i)


# range with (start, stop, step)
for i in range(2,10,3):  # range(start, stop, step)
    print(i)


# print all the even numbers between 2 & 100
for i in range(2, 101, 2):
    print(i)


# print all the odd numbers between 2 & 100
for i in range(3, 100, 2):
    print(i)