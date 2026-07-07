# question1: write a program to count the number of students with the "A" grade in the following tuple. 
# question2: store the given tuple in a list & sort them from "A" to "D".


# solution of question1 and question2 
tuple = ("C", "D", "A", "A", "B", "B", "A")
count = tuple.count("A")

print("Number of students with A grade: ", count)

tuple_list = list(tuple)
tuple_list.sort()
print("sorted_list: ", tuple_list)