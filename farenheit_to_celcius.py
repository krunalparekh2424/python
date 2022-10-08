#this program is to convert farenheit to celcius
#(1°F − 32) × 5/9 
farenheit = input("enter farenheit temp to convert ")
farenheit = int(farenheit)
celcius = (farenheit - 32) * (5/9)
print(celcius)