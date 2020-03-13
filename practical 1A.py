# Python program to read and write files
# Write data in files
file1=open("myfile.txt","w")
file1.write("python programing\n")
#  \n is placed to indictae EQL
file1.write("Pp\n This is our first practical\n We have to read nd write line\nfull form of pp is python programing")
file1.close()  # To change file access modes

file1=open("myfile.txt","r+")
print("output of read function is")
print(file1.read())

# Seek(n) takes the file handle to the nth bite from the start
file1.seek(0)
print("output of readline function is")
print(file1.readline())

# Seek(n) takes the file handle to the nth bite from the start
file1.seek(0)
print("output of read(5) function is")
print(file1.read(5))

# Seek(n) takes the file handle to the nth bite from the start
file1.seek(0)
print("output of readline(5) function is")
print(file1.readline(5))

# Seek(n) takes the file handle to the nth bite from the start
file1.seek(0)
print("output of readlines function is")
print(file1.readlines())
file1.close()  #To change file access modes
