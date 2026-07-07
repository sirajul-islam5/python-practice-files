collection = set()

collection.add(1)
collection.add(2)
collection.add(2) # duplicate value will not be added to the set
collection.add("johncollege")
collection.add((4, 5, 6)) # adding a tuple to the set

collection.remove(1) # removes the specified value from the set

print(collection)
print(type(collection))
print(len(collection))

collection.clear() # removes all the items from the set
print(len(collection))



another_collection = {"hello", "johncollege", "world", "coding", "python"}
print(another_collection)
print(another_collection.pop()) # removes and returns a random item from the set
print(another_collection.pop())


# union method - returns a new set that contains all the items from both sets
set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2)) # {1, 2, 3, 4}
print(set1)
print(set2)

# intersection method - returns a new set that contains only the items that are present in both sets
print(set1.intersection(set2)) # {2, 3}