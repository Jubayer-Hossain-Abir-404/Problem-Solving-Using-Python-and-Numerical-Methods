def Gauss(p,n1):
    a=[[2,1,-1],[-3,-1,2],[-2,1,2]]
    b=[8,-11,3]
    x=[]
    n=3
    if(a[0][0]!=0):
        for k in range(0,n-2):
            for i in range(k+1,n-1):
                factor=a[i][k]/a[k][k]
            for j in range(0,n-2):
                a[i][j]=a[i][j]-factor*a[k][j]
            b[i]=b[i]-factor*b[k]


        x[n-1]=b[n-1]/a[n-1][n-1]
        for i in range(n-2,1,-1):
            sum=b[i]
            for j in range(i+1,n-1):
                sum=sum-a[i][j]*x[j]
            x[i]=sum/a[i][i]


        print x
        
            

def main():
    Gauss(3,3)


if __name__=="__main__":
    main()
