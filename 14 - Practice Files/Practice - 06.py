# question-1: store following word meanings in a python dictionary:
      # table: "a piece of furniture", "list of facts & figures"
      # cat: "a small animal"

dictionary = {
    "table": ["a piece of furniture", "list of facts & figures"], 
    "cat": "a small animal"
}

print(dictionary)



# question-2: you are given a list of subjects for students. assume one classroom is required for 1 subject. how many classrooms are needed by all students.
     # python, java, c++, python, javascript, java, python, java, c++, c 

subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}

print(subjects)
print(len(subjects)) # 5 classrooms are needed for all students. 



# question-3: write a program to enter marks of 3 subjects from the user and store them in a dictionary. 
# start with an empty dictionary & add one by one. use subject name as key & marks as value. 
# first method: using input function to get marks from the user.
marks = {} 
print(marks) 

marks["python"] = 95
marks["sql"] = 88
marks["power bi"] = 90 

print(marks)
# second method: using update method to add marks in the dictionary.
marks2 = {}
print(marks2)

x = int(input("enter python marks: "))
marks2.update({"python": x})

x = int(input("enter sql marks: "))
marks2.update({"sql": x})

x = int(input("enter power bi marks: "))
marks2.update({"power bi": x})

print(marks2)