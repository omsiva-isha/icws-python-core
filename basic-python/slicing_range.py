print("Try programiz.pro")


my_list = [10, 20, 30, 40, 50, 60]
my_string = "Sivanesan Mathivanan"
my_name="mathivanan"
str1="kumutha"
str2="ranjana"
poli="madam"

# mutha muk
#jana nar
print(str1[2:])
print(str1[2::-1])
print(str2[3:])
print(str2[2::-1])
# my_string[start:stop]
# my_string[start:stop:step]

# Basic slicing
print(my_string[0:9])  # Output: Sivanesan
print(my_list[1:4])    # Output: [20, 30, 40]
print(my_string[10:15])

# Omitting start or stop
print(my_string[:4])   # Output: Sivanesan (starts from beginning)
print(my_list[3:])     # Output: [40, 50, 60] (goes to end)
print(my_string[3:])     # Output: [40, 50, 60] (goes to end)
print(my_string[:])    # Output: Sivanesan Mathivanan (creates a full copy)

# Using step
print(my_list[::2])    # Output: [10, 30, 50] (every other element)
print(my_string[::-1]) # Output: gnicilS nohtyP (reverses the string)

# Negative indexing
print(my_list[-2:])    # Output: [50, 60] (last three elements)()
print(my_string[:-10]) # Output: sivanesan (excludes the last 10 characters)

# range(stop) max stop-1
# range(start,stop) max stop -1
# range(start,stop,incr/dec)
print(list(range(6)))
print(list(range(1,6)))
print(list(range(1,6,2)))
print(list(range(6,-1,-1)))
print(list(range(11,6,-1)))

#21 to 29 next 17,16...10

print(list(range(21,30)))
print(list(range(17,9,-1)))


a="madam"
b="ranjana"
c="malayalam"
print(a==a[::-1])
print(b==b[::-1])
print(c==c[::-1])