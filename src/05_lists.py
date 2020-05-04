# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
a = x
a.append(4)
print(a)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

b = x
for i in y:
    b.append(i)

print(b)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
c = x
c.remove(8)

print(c)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
d = x
d.insert(5, 99)
print(d)

# Print the length of list x
# YOUR CODE HERE

print(len(x))

# Print all the values in x multiplied by 1000
# YOUR CODE HERE

e = x

for i in e:
    print(i*1000)
