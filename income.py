# 2) Write a Python program to calculate & display income tax, gross income, net income from monthly income given by user 

# yearly income     tax rate
# <3,00,000         5%  

# >=3,00,000
# <5,00,000         10%  

# >=5,00,000
# <8,00,000         20%

# >=8,00,000        30%
income = int(input("enter your monthly income "))
print(income)
#converting monthly income to yearly income
yearly_income = income * 12
print("your yearly income is",yearly_income)

