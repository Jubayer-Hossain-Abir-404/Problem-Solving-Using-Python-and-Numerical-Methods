def linear(x,y,x1):
    n=0
    for i in range(0,6-1):
        if(x1>=x[i]):
            if(x1<=x[i+1]):
                n=i
                break
    b0=y[n]
    print "b0:",b0
    b1=(y[n+1]-y[n])/(x[n+1]-x[n])
    print "b1:",b1
    ans=b0+b1*(x1-x[n])
    print ans
    print "After expanding:"
    b=b0+b1*(-x[n])
    print b,"+",b1,"*x"

def main():
    x=[0,10,15,20,22.5,30]
    y=[0,227.04,362.78,517.35,602.97,901.67]
    x1=input("Determine the value:")
    linear(x,y,x1)


if __name__=="__main__":
    main()
