#elctricity bill with tax and total bill
unit = int(input("Enter your consumed unit: "))
print("you have consumed total",unit,"unit \nNow let us count your bill amount")
if unit<=100:
   total_amount = unit*1
   print("your bill amount is ",total_amount,"*")
elif unit>101 and unit<=200:
   total_amount = unit*2
   print("your bill amount is ",total_amount,"*")
elif unit>201 and unit<=300:
   total_amount = unit*3
   print("your bill amount is ",total_amount,"*")
elif unit>301 and unit<=400:
   total_amount = unit*4
   print("your bill amount is ",total_amount,"*")  
elif unit>400:
   total_amount = unit*5
   print("your bill amount is ",total_amount,"*")    
print("10% additional charges will be count now ")
charges = total_amount * 10 / 100
final_amount = total_amount + charges
print("your total bill amount is ",final_amount,"\nThank you for using PGVCL")

