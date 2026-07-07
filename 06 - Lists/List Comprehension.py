import random
import string

pass_len = 12 
charValues = string.ascii_letters + string.digits + string.punctuation 

# list comprehension [function for item in iterator] / [function for i in range(n)]

password = "".join([random.choice(charValues) for i in range(pass_len)])
print("your random password is: ", password)


