#write a program to find largest rectangle with user input
length1 = int(input("enter length for first shape "))
width1 = int(input("enter width for first shape "))
#data for shape 2 
length2 = int(input("enter length for second shape "))
width2 = int(input("enter width for second shape "))
area1 = width1 * length1  
print("Area of first shape is ", area1)

area2 = width2 * length2  
print("Area of second  shape is ", area2)
if area1 > area2:
    print("first rectangle is largest ")
else: 
    print("second rectangle is largest ")