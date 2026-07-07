# uses of continue (continue acts as skip)
i = 0
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1
print("loop ended")


# count 1 to 10 but skip the even values
i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue 
    print(i)
    i += 1
print("loop ended")


# count 1 to 10 but skip the odd values
i = 1
while i <= 10:
    if(i%2 == 1):
        i += 1
        continue
    print(i)
    i += 1
print("loop ended")
