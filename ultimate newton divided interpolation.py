def newton(x,y,n,x1):
    b=[0.0]*(n+1)
    for i in range(0,n+1):
        if(i==0):
            b[i]=y[i]
        elif(i==1):
            b[i]=((y[i]-b[i-1])/(x[i]-x[0]))
        elif(i==2):
            b[i]=(((y[i]-y[i-1])/(x[i]-x[i-1]))-b[i-1])/(x[i]-x[0])
        else:
            bm=(((y[i]-y[i-1])/(x[i]-x[i-1]))-((y[i-1]-y[i-2])/(x[i-1]-x[i-2])))/(x[i]-x[i-2])
            b[i]=(bm-b[i-1])/(x[i]-x[0])
    sum=b[0]
    Mu=1.0
    for i in range(0,n):
        for j in range(0,i+1):
            Mu=Mu*(x1-x[j])
        sum=sum+b[i+1]*Mu
        Mu=1.0

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

    newton(x,y,n,x1)

if __name__=="__main__":
    main()
