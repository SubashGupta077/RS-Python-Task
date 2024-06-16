#10. Given a 2D integer array matrix, return the transpose of matrix.And give  its transpose.
a=int(input('enter row '))
b=int(input('enter column '))
array=[[1 for _ in range(b)] for _ in range(a)]
array1=[[1 for _ in range(a)] for _ in range(b)]
for i in range(0,a):
    for j in range (0,b):
        m=int(input(f'enter the {j+1} element of {i+1} row :'))
        array[i][j]=m
        array1[j][i]=m
print('Input Matrix = ',array)
print('Output Matrix = ',array1) 
