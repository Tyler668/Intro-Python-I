"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file
# Note: pay close attention to your current directory when trying to open "foo.txt"

# YOUR CODE HERE
with open("C:\\Users\\tyler\\Documents\\github\\Intro-Python-I\\src\\foo.txt", "r") as f:
    print(f.read())



# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open("C:\\Users\\tyler\\Documents\\github\\Intro-Python-I\\src\\bar.txt", 'w') as f2:
    f2.write("Hello\n")
    f2.write("Testing\n")
    f2.write("123")

with open("C:\\Users\\tyler\\Documents\\github\\Intro-Python-I\\src\\bar.txt", 'r') as f3:
   print(f3.read())