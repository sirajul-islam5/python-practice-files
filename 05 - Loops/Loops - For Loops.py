# uses of for loops 
nums = [1, 2, 3, 4, 5]
subjects = ["python", "power bi", "sql", "excel"]
tup = (10, 20, 30, 40, 50)
str = ("johncollege")

for val in nums:
    print(val)

for val in subjects:
    print(val)

for val in tup:
    print(val)

for char in str:
    print(char)
else:
    print("end")


# use else in for loops 
str = "johncollege"

for char in str:
    if(char == "o"):
        print("o found")
        break
    print(char)
else:
    print("end")