def f1(xdown,xup):
    return ((0.2*xup)+(25*pow(xup,2)/2.0)-(200*pow(xup,3)/3.0)+(675*pow(xup,4)/4.0)-(900*pow(xup,5)/5.0)+(400*pow(xup,6)/6.0))-((0.2*xdown)+(25*pow(xdown,2)/2.0)-(200*pow(xdown,3)/3.0)+(675*pow(xdown,4)/4.0)-(900*pow(xdown,5)/5.0)+(400*pow(xdown,6)/6.0))

def f(x):
    return 0.2+25*x-200*pow(x,2)+675*pow(x,3)-900*pow(x,4)+400*pow(x,5)


def simpson(a,b,n):
    simp=f(a)
    h=(b-a)/float(n)
    for i in range(1,n):
        if(i%2!=0):
            simp=simp+4*f(a+i*h)
    for i in range(2,n-1):
        if(i%2==0):
            simp=simp+2*f(a+i*h)
    simp=simp+f(b)
    simp=simp*(b-a)/float(3*n)
    Et=f1(a,b)-simp
    inter=f1(a,b)
    Etabs=abs(((inter-simp)/inter)*100)
    print "x:",f1(a,b)
    print "I:",simp
    print "\nn:",n," I:",simp," Et:",Et," Et(%):",Etabs

def main():
    a=input("Print the lower limit:")
    b=input("print the upper limit:")
    n=input("Input the number of segment:")
    simpson(a,b,n)


if __name__=="__main__":
    main()
