row=3
col=3
matrix=[[1,2,3],[4,5,6],[7,8,9]]
matrix_1=[[1,2,3],[4,5,6],[7,8,9]]
matrix_2=[[0,0,0],[0,0,0],[0,0,0]]
print matrix[0]
print matrix[1]
print matrix[2]
print "-----Matrix-----"
print matrix_1[0]
print matrix_1[1]
print matrix_1[2]
print "-----Matrix Addition-----"

for i in range(0,row):
    for j in range(0,col):
        matrix_2[i][j]=matrix[i][j]+matrix_1[i][j]


for i in range(0,row):
    print matrix_2[i]
