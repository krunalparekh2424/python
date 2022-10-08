#this code is to calculate simple intrest for given amount year & rate

principal = input("enter your amount ")
print("your amount is ",principal)
principal = int(principal)
rate = input("enter your desired rate ")
rate = int(rate)
time = input("kindly enter your loan tenure in year/s ")
time = int(time)
print("you selected loan for",time,"yeras of rs",principal,"at",rate,"% intrest rate")
si = principal*rate*time/100
print("your simple intrest for selected option will be",si)
print("thank you for using our service")