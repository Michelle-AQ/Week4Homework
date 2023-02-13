# Using the open and read methods to slurp and reading the entire contents of the file 'pelican.txt'
with open("pelican.txt") as f:
    contents = f.read()
    # Printing the type of the returned data
print(type(contents))
# Printing the contents of the pelican.txt file
print(contents)
# The data type is a string

# Write some code that will read the pelican.txt file into a list and then output the number of items within the list
with open('pelican.txt') as f:
    f = f.readlines()
    print(f)
    print(type(f))
    print(len(f))

# After the strip method, no blank spaces
for i in f:
    print(i.rstrip())