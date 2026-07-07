info = {
    "key" : "value",
    "name" : "john college",
    "subject" : ["python", "power bi", "sql"],
    "topics" : ("dictionary", "list", "tuple"),
    "learning" : "programming",
    "age" : 20,
    "is student" : True,
    "marks" : 94.4
}

print(info)
print(type(info))

print(info["name"])
print(info["subject"])
print(info["topics"])
print(info["age"])

info["name"] = "john university"
print(info)

info["city"] = "oslo"
print(info)

null_dict = {}
print(null_dict)

null_dict["city"] = "copenhagen"
print(null_dict)