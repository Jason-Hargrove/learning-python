thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)


# What is the proper code for creating a "for" loop that will execute 9 times starting at the number 6?
def loop_over():
    for i in range(6, 15):
        print(i)
4
loop_over()


# What will this line do?
# value=input("2+2=")


# What will the following code print?
def inc(a,b=1):
    return(a+b)

 a=inc(1)
 a=inc(a,a)
 print(a)