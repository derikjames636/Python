#increasing triangle

number_of_rows=int(input('Enter the number of rows'))
for i in range(number_of_rows+1):
    for j in range(i):
        print('*',end="")
    print()

#Decreasing triangle

number_of_rows = int(input('Enter number rows'))
for i in range(number_of_rows, 0, -1):
    for j in range(i):
        print('*', end="")
    print()

#hill pattern

number_of_rows=int(input('Enter the number of rows'))
for i in range(1,number_of_rows+1):
    for j in range(number_of_rows-i):
        print(' ',end=" ")
    for k in range (2*i-1):
        print('*',end=" ")
    print()
#reverse hill pattern
number_of_rows=int(input('Enter the number of rows'))
for i in range(number_of_rows,0,-1):
    for j in range(number_of_rows-i):
        print(' ',end=" ")
    for k in range (2*i-1):
        print('*',end=" ")
    print()





