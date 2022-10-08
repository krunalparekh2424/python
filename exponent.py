#this program is to find exponent of input from user 
base = int(input("enter your base number "))
power = int(input("enter your power number "))
print("if enterd number is negetive we will turn that into positive for you")
if base<0 and power<0:
    base = 0 - base
    power = 0 - power
exoponent = base ** power
print("your exponent is",exoponent)
print("thank you for using services")