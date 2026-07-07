# Palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward



# example 1
list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("list1 is a palindrome")
else: 
    print("list1 is not a palindrome")


# example 2
list2 = [1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("list2 is a palindrome")
else:
    print("list2 is not a palindrome")