def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993

def secant(xi_minus,xi,Es):
    Ea=1000.0
    n=0
    print "Iteration\t\t\txi_minus\t\t\txi\t\t\txi_plus\t\t\tEa"
    while(Ea>Es):
        xi_plus=xi-(f(xi)*(xi-xi_minus))/(f(xi)-f(xi_minus))
        Ea=(xi_plus-xi)/xi_plus
        Ea=abs(Ea)*100
        print n+1,"\t\t\t",xi_minus,"\t\t\t",xi,"\t\t\t",xi_plus,"\t\t\t",Ea
        xi_minus=xi
        xi=xi_plus
        n+=1

def main():
    xi_minus=input("Enter the lower value:")
    xi=input("Enter the upper value:")
    es=input("Enter the pre specified error:")
    secant(xi_minus,xi,es)

if __name__=="__main__":
    main()
