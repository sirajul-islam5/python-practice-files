# with open("Demo on Python.txt", "r") as f:
#     data = f.read()
#     print(data)

# with open("Demo on Python.txt", "w") as f:
#     f.write("new data")

# with open("Practice - 16.py", "w")as f:
#     f.write("Hi everyone\nWe are learning File I/O\n")
#     f.write("using Python\nI like programming in Python")

# with open("Practice - 16.py", "r") as f:
#     data = f.read()
# new_data = data.replace("Python", "Java")
# print(new_data)

# with open("Practice -16.py","w") as f:
#     f.write(new_data)



# def check_for_word(word):
#     with open("Practice - 16.py", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("Not Found")

# check_for_word("learning")

# question: write a function to find in which line of the file does the word "learning" occur first. print -1 if the word not found 
def check_for_line():
    word = "learning"
    data = True
    line_no = 1 
    with open("Practice - 16.py","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

print(check_for_line())
