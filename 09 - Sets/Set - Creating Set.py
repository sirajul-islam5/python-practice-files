# set is the collection of the unordered items. each element in the set must be unique & immutable. but set itself is mutable. 
collection = {1, 2, 3, 4, "hello", "world"}

print(collection)
print(type(collection))
print(len(collection)) # total number of items in the sety

empty_collection = {}
print(empty_collection)
print(type(empty_collection)) # this is not a set, it's a dictionary

empty_set = set()
print(empty_set)
print(type(empty_set)) # this is a set
