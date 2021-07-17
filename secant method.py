def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993

def secant(xi_minus,xi,i):
    print "Iteration\t\txi_minus\t\txi\t\txi_plus\t\tEa(%)"
    n=0
    while(n<i):
        xi_plus=xi-(f(xi)*(xi-xi_minus))/(f(xi)-f(xi_minus))
        Ea=(xi_plus-xi)/xi_plus
        if(Ea<0):
            Ea*=-1
        Ea*=100
        print n+1,"\t\t",xi_minus,"\t\t",xi,"\t\t",xi_plus,"\t\t",Ea
        xi_minus=xi
        xi=xi_plus
        n+=1


def main():
    secant(0.02,0.05,3)

if __name__=="__main__":
    main()
        
