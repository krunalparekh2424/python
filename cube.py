#write a program to print following pattern 
# 1 8 27 64 125 ..... 1000

number = 1
cube = number*number*number
print(cube)
while number<=1000:
    cube = number * number * number
    print(cube)
    number = number + 1
print("loop ended \ngood day.....")