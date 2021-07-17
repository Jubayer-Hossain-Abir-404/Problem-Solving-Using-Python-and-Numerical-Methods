def lagrange(x,y,n,x1):
    sum=0.0
    Lt=1.0
    for i in range(0,n+1):
        for j in range(0,n+1):
            if(j!=i):
                Lt=float(Lt*((x1-x[j])/(x[i]-x[j])))
        sum=sum+float(Lt*y[i])
        Lt=1.0

    print "The result is:",sum


def main():
    n=input("Input the value of n:")
    x=[0.0]*(n+1)
    y=[0.0]*(n+1)
    for i in range(0,n+1):
        x[i]=float(input("Input the value of x:"))
    for i in range(0,n+1):
        y[i]=float(input("Input the value of y:"))
    x1=float(input("Determine the value:"))
    lagrange(x,y,n,x1)


if __name__=="__main__":
    main()
    
