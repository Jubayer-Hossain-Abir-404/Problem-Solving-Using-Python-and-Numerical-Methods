def linear(x,y,x1):
    n=0
    for i in range(0,6-2):
        if(x1>=x[i]):
            if(x1>=x[i+1]):
                if(x1<=x[i+2]):
                    n=i
                    break
    b0=y[n]
    print "b0:",b0
    b1=(y[n+1]-y[n])/(x[n+1]-x[n])
    print "b1:",b1
    b2=(((y[n+2]-y[n+1])/(x[n+2]-x[n+1]))-((y[n+1]-y[n])/(x[n+1]-x[n])))/(x[n+2]-x[n])
    print "b2:",b2
    ans=b0+b1*(x1-x[n])+b2*(x1-x[n])*(x1-x[n+1])
    print ans
    print "After expanding:"
    b=b0+b1*(-x[n])+b2*(-x[n])*(-x[n+1])
    c=b1+b2*(-x[n])+b2*(-x[n+1])
    print b,"+",c,"*x+",b2,"*x^2"

def main():
    x=[0,10,15,20,22.5,30]
    y=[0,227.04,362.78,517.35,602.97,901.67]
    x1=input("Determine the value:")
    linear(x,y,x1)


if __name__=="__main__":
    main()
