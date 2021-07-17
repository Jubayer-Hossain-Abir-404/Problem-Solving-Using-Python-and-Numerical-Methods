n=input("What should be the dimension of the matrix:")
a=[0]*n
for i in range(0,n):
    a[i]=[0]*n

print "Matrix of Coefficient"
for i in range(0,n):
    for j in range(0,n):
        a[i][j]=input("Enter Value:")


b=[0]*n
print "Constant Vector"
for i in range(0,n):
    b[i]=input("Enter Value:")

for i range(0,n-1):
    for j in range(i+1,n):
        for k in range(i+1,n):
            if(a[j][k]

for i in range(0,n-1):
    for j in range(i+1,n):
        factor=a[j][i]/a[i][i]
        for k in range(i+1,n):
            a[j][k]=a[j][k]-factor*a[i][k]
        b[j]=b[j]-factor*b[i]


x=[0]*n
x[n-1]=b[n-1]/a[n-1][n-1]
i=n-2
while(i>=0):
    sum=b[i]
    for j in range(i+1,n):
        sum=sum-a[i][j]*x[j]
    x[i]=sum/a[i][i]
    i=i-1


print "Vector of Variable"
for i in range(0,n):
    print x[i]
        
               
