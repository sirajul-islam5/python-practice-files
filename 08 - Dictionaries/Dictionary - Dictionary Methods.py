# dictionary don't allow duplicate keys 
student = {
    "name" : "abdullah",
    "subjects" : {
        "python" : 90,
        "sql" : 85,
        "power bi" : 88
    }
}

print(student.keys())

# keys method - returns all the keys in the dictionary
print(list(student.keys()))
print(len(list(student.keys())))

# values method - returns all the values in the dictionary
print(student.values())

# items method - returns all the key-value pairs in the dictionary
print(student.items())
print(list(student.items()))

# making pairs of key-value in the dictionary
pairs = list(student.items())
print(pairs)
print(pairs[0])
print(pairs[0][0]) # key
print(pairs[0][1]) # value

# get method - returns the value of the specified key
print(student["name"])
print(student.get("name")) 

# print(student["name2"]) # error
# print(student.get("name2")) # not error, returns None

# update method - updates the value of the specified key
student.update({"city" : "shenzhen" , "age" : 21})
print(student)