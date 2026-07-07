light = "scarlet"

if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("wait")
elif(light == "green"):
    print("go")
else:
    print("light is not working")

print("program ended")

num = 5 
if(num > 2):
    print("greater than 2")
elif(num > 3):
    print("greater than 3")
else:
    print("less than or equal to 2")

# indentation = 4 spaces or 1 tab before the statement

# codithion statement in the exam marks:
marks = int(input("enter student marks: "))

if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks < 90):
    print("grade B")
elif(marks >= 70 and marks < 80):
    print("grade C")
elif(marks < 70):
    print("grade D")