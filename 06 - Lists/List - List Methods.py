list = [2, 1, 3,]

list.append(4) # adds an element to the end of the list
print(list)

list.sort() # sorts the list in ascending order
print(list)

list.sort(reverse=True) # sorts the list in descending order
print(list)



fruits = ["banana", "orange", "apple"]

fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)



numbers = [5, 1, 9, 1]

numbers.reverse() # reverses the original order of the list
print(numbers)

numbers.insert(1, 10) # inserts an element at a specific index
print(numbers)

numbers.sort()
print(numbers)

numbers.remove(1) # removes the first occurrence of the specified value
print(numbers)

numbers.pop(2) # removes and returns the element at the specified index
print(numbers)