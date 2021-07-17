row=3
col=3
a=[0]*col  #it means [0]*3=[0,0,0]. ekta matrix er ekta row te 3 ta column create kora
for i in range(0,row):
    a[i]=[0]*col  #ata dea bujacche a[0] er moddhe 3 ta column .a[1] er moddhe 3 ta column abr a[2] er moddhe 3 ta column.
print "1st Matrix:"
for i in range(0,row):
    for j in range(0,col):
        a[i][j]=input("Enter value:")

b=[0]*col
for i in range(0,row):
    b[i]=[0]*col

print "2nd Matrix:"
for i in range(0,row):
    for j in range(0,col):
        b[i][j]=input("Enter Value:")

c=[[0,0,0],[0,0,0],[0,0,0]]


for i in range(0,row):
    for j in range(0,col):
        sum=0
        for k in range(0,col):
            sum=sum+a[i][k]*b[k][j]
        c[i][j]=sum

print "Matrix Multiplication:"
for i in range(0,row):
    print c[i]
