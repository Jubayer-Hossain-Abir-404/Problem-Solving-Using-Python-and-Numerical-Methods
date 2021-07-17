def f1(xdown,xup):
    return ((0.2*xup)+(25*pow(xup,2)/2.0)-(200*pow(xup,3)/3.0)+(675*pow(xup,4)/4.0)-(900*pow(xup,5)/5.0)+(400*pow(xup,6)/6.0))-((0.2*xdown)+(25*pow(xdown,2)/2.0)-(200*pow(xdown,3)/3.0)+(675*pow(xdown,4)/4.0)-(900*pow(xdown,5)/5.0)+(400*pow(xdown,6)/6.0))

def f(x):
    return 0.2+25*x-200*pow(x,2)+675*pow(x,3)-900*pow(x,4)+400*pow(x,5)


def trapezoid(a,b,n):
    tramp=0
    h=(b-a)/float(n)
    if(n==1):
        tramp=tramp+(((b-a)/2*n)*(f(a)+f(b)))
    elif(n>1):
        tramp=f(a)
        for i in range(1,n):
            tramp=tramp+2*f(a+i*h)
        tramp=tramp+f(b)
        tramp=((b-a)/float(2*n))*tramp
    Et=f1(a,b)-tramp
    inter=f1(a,b)
    Etabs=abs(((inter-tramp)/inter)*100)
    print "x:",f1(a,b)
    print "I:",tramp
    print "\nn:",n," I:",tramp," Et:",Et," Et(%):",Etabs


def main():
    a=input("Print the lower limit:")
    b=input("print the upper limit:")
    n=input("Input the number of segment:")
    trapezoid(a,b,n)


if __name__=="__main__":
    main()
