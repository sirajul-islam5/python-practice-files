# Tuples are immutable, so we cannot modify them directly
# However, we can create a new tuple by concatenating existing tuples

tup = (2, 1, 3, 1)
print(type(tup)) # <class 'tuple'>
print(tup[0:3]) # (2, 1, 3)

print(tup[0]) # 2
print(tup[1]) # 1

empty_tuple = ()
print(empty_tuple) # ()

single_element_tuple = (42,)
print(single_element_tuple) # (42,)
print(type(single_element_tuple)) # <class 'tuple'>

simgle_element_tuple_without_comma = (42)
print(simgle_element_tuple_without_comma) # 42
print(type(simgle_element_tuple_without_comma)) # <class 'int'>