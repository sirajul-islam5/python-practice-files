# Creating Nested Dictionary
student = {
    "name" : "abdullah",
    "subjects" : {
        "python" : 90,
        "sql" : 85,
        "power bi" : 88
    }
}

print(student)
print(student["subjects"])
print(student["subjects"]["python"])