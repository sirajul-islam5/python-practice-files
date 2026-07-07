# Figur out a way to store 9 & 9.0 as seprate values in the set. (You can take help of built-in data types)

# method1:
values = {9, "9.0"}
print(values)

# method2:
values2 = {
    ("float", 9.0),
    ("int", 9)
}
print(values2)