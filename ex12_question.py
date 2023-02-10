tup = 'Hello'
print(len(tup))
# The 'Hello' string is being counted by how many items are in the string e.g. letter
# The absence of a comma means that each individual part of the string is being counted
# The print function prints the length of the tuple
#  count number is 5

tup = 'Hello',
print(len(tup))
# The trailing comma after 'Hello' causes the tuple to be grouped as one object
# This causes the 'len' to count 'Hello' as one object instead of individual objects
# The print function prints the length of the tuple
# count number is 1

# To test this out, another 'Hello' string was added to the tuple
tup = 'Hello', 'Hello'
print(len(tup))
# The trailing comma between 'Hello' causes len to count the different 'Hello's as two grouped objects
# The print function prints the length of the tuple
# count number is 2

