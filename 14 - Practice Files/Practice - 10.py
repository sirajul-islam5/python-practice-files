# question1: print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in nums:
    print(val)


# question2: search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
# methond1:
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49
for val in nums:
    if(val == x):
        print("FOUND!", x)
        break
else:
    print("NOT FOUND")

# method2: # linear search 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49 
idx = 0
for val in nums:
    if(val == x):
        print("number found at idx", idx)
        break
    idx += 1