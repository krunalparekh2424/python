#print following pattern 
'''
54321
4321
321
21
1
'''
from itertools import count


column = 1 
while column<=5:
    row = 5
    count = 5
    while row>=column:
        print(count,end=" ")
        row = row - 1
        count = count - 1
    print("")
    column = column + 1



