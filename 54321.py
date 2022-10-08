#write a following pattern 
'''
5
54
543
5432
54321
'''
row = 5
while row>=1:
    column=5
    while column>=row:
        print(column,end=" ")
        column = column - 1
    print("")
    row = row - 1
