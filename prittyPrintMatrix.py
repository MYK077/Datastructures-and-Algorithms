# A 5 x 7 multiplication table looks like this:
# printMatrix(5, 7):
#
#       0	1	2	3	4	5	6	7
#   ----	----	----	----	----	----	----	----
#   0	0	0	0	0	0	0	0	0
#   1	0	1	2	3	4	5	6	7
#   2	0	2	4	6	8	10	12	14
#   3	0	3	6	9	12	15	18	21
#   4	0	4	8	12	16	20	24	28
#   5	0	5	10	15	20	25	30	35

# printMatrix(1, 1):
#      0     1
#      ---   ---
# 0    0     0
# 1    0     1

# Write a function to “pretty print” a multiplication table.

def getMatrix(rows, cols):
    x = []
    for row in range(0,rows):
        x.append([0]*cols)

    for row in range(1, rows):
        for col in range(1, cols):
            x[row][col] = row + x[row][col-1]
    return x

def prettyPrint(array):
    print('--1, 2, 3, 4, 5, 6, 7')
    count = 1
    for x in array:
        print(count, x)
        count+=1

prettyPrint(getMatrix(5,7))
