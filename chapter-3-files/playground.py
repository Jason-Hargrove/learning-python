# thestr = "Ogres are often foolhardy oafs"
# newstr = ""
# for i, c in enumerate(thestr):
#     if c == "o":
#         continue
#     if i > 20:
#         break
#     newstr += c
# print(newstr)


# What is the proper code for creating a "for" loop that will execute 9 times starting at the number 6?
# def loop_over():
#     for i in range(6, 15):
#         print(i)
# 4
# loop_over()


# What will this line do?
# value=input("2+2=")


# What will the following code print?
# def inc(a,b=1):
#     return(a+b)

# a=inc(1)
# a=inc(a,a)
# print(a)


# What is the proper syntax for accessing the fourth element of the following sequence?
# values = [1,3,5,7,9,11,13]
# print(values[3])


# What will be the result of the following code?
# thestr = "This is a string"
# print(thestr)
# thestr = 5


# What will this code print?
# try:
#     x=int("five")
# except ValueError:
#     print("There is a value error.")
# finally:
#     print("Something went wrong.")


# For Chapter 3 Code Challenge
import os

def file_info():
    directory = "./deps"
    total_size = 0
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if filepath.endswith(".txt"):
            total_size += os.path.getsize(filepath)
    return total_size