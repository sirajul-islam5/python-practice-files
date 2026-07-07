str = "i am studying Python programming from johncollege"
str = str.capitalize() #capitalizes the first character of the string and returns a new string

print(str.endswith("ege")) #returns True if the string ends with "ege" 

print(str.endswith("app")) #returns False if the string does not end with "app"

print(str.capitalize()) #capitalizes the first character of the string

print(str)

print(str.replace("o", "a")) #replaces all occurrences of "o" with "a" and returns a new string
print(str.replace("python", "javascript"))

print(str.find("o")) #returns the index of the first occurrence of "o" in the string
print(str.find("Q")) #returns -1 if "Q" is not found in the string
print(str.find("from")) #returns the index of the first occurrence of "from" in the string

print(str.count("from")) #returns the number of occurrences of "from" in the string