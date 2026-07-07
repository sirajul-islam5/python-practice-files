# question1: print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
print("loop ended")



# question2: print the elements of the folllowing list using a loop: ["batman","ironman", "spiderman", "thor", "superman"]
superheroes = ["batman","ironman", "spiderman", "thor", "superman"]
idx = 0 # initialization 
while idx < len(superheroes): # stopping condition 
    print(superheroes[idx])
    idx += 1
print("loop ended")         #traverse = to travel[whole process done in that question]



# question3: search for a number x in this tuple using loop: (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

# first see the normal task 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0 # initialization 
while i < len(nums):
    print(nums[i])
    i += 1 
print("loop ended")

# now back to the main question 
nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36 
i = 0 
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx", i)
        break
    else:
        print("finding ..")
    i += 1 
print("loop ended")