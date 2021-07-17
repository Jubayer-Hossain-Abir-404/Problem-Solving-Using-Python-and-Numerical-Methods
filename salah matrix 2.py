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
        c[i][j]=a[i][j]+b[i][j]

print "Matrix Addition:"
for i in range(0,row):
    print c[i]
