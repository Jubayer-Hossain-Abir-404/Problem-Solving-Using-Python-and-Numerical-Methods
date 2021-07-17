def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993
def f_prime(x):
    return 3*pow(x,2)-0.165*2*x
def newton(xi,i):
    print "Iteration\t\t\t\txl\t\t\t\txu\t\t\tEa(%)"
    n=0
    while(n<i):
        xi1=xi-(f(xi)/f_prime(xi))
        Ea=(xi1-xi)/xi1
        if(Ea<0):
            Ea*=-1
        Ea*=100
        print n+1,"\t\t\t",xi,"\t\t\t\t",xi1,"\t\t\t",Ea
        xi=xi1
        n+=1



newton(0.05,4)
