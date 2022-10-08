#find weather shape is square or not
length = int(input("enter length for shape "))
width = int(input("enter width for shape "))
print(f"your length is {length}, \nAnd width is {width},")
if length == width:
    print("this shape is square")
else:
    print("this shape is not square")