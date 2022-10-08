#write squareroot for every num.
#1 4 9 16 25 36 49 .... 100

number = 1
square = number*number 
print(square)
while number<=100:
    square = number * number
    number = number + 1
    print(square)
print("loop ended \ngood day.....")
