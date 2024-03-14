# just say open to open or read a file

my_file = open('/Users/sriyansrauniyar/Desktop/ZTM/Python Developer/ZTM---Python-Developer/Python Introduction:Basics/oopnotes.txt')

# file.read() gives the content of the file
print(my_file.read())

# now that Python has used a cursor to read the given file. The cursor moves to the end. So, if I say my_file.read() again, nothing
# gets printed. To counter that, say my_file.seek(0) which moves the cursor back to the very top. 

my_file.seek(0)
print(my_file.read())

my_file.seek(0)
# reads one line at a time
print(my_file.readline())

my_file.seek(0)
# gives a list of all lines 
print(my_file.readlines())

# at the end, you gotta close the file 
my_file.close()


# by default, mode is read only. You can change that by adding mode manually to 'r+' 
next_file = open('/Users/sriyansrauniyar/Desktop/ZTM/Python Developer/ZTM---Python-Developer/Python Introduction:Basics/oopnotes.txt', mode='r+')
# Caution though, this overwrites the existing text in a file since cursor begins from position 0
next_file.write('hey, how you doing man!')

next_file.close()

# so, rather use an append mode 'a' to append to the end of the file 
next1_file = open('/Users/sriyansrauniyar/Desktop/ZTM/Python Developer/ZTM---Python-Developer/Python Introduction:Basics/oopnotes.txt', mode='a')
# now, this gets appended to the very end of the file
next1_file.write('hey, how you doing man!')

next1_file.close()

# if you used 'w' mode, it will overwrite everything with whatever you want to write. So, be careful. But, if the file name doesn't exist, 
# w creates that new file

# Common errors is FileNotFoundError or IOError