# -*- coding: utf-8 -*-
"""

@author: Nattapat Tangniyom 640631032
"""

# input example : 5 6
m,n = input("Enter the numbers of m and n: ").split()
m = int(m)
n = int(n)
matrix = []
for i in range(m):
    arr = []
    for j in range(n):
        if i<j and j!=m-1 :
            arr.append(0)
        elif i==j or j==m-1:
            arr.append(1)
        else:
            arr.append(-1)
    matrix.append(arr)
print(matrix)

"""
input example : 5 6
result : [[1, 0, 0, 0, 1, 0], [-1, 1, 0, 0, 1, 0], [-1, -1, 1, 0, 1, 0], [-1, -1, -1, 1, 1, 0], [-1, -1, -1, -1, 1, 0]]
"""
