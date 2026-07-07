# question: write a recursive function to print all elements in a list (hint: use list & index as parameters)
def print_list(list, idx = 0):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango", "lichi", "apple", "banana"]

print_list(fruits) 