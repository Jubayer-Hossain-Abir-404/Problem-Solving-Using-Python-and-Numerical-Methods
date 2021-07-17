def g(x):
    return (-0.88318*pow(10,-2))/(-0.50598*pow(10,-10)*pow(x,2)+0.38292*pow(10,-7)*x+0.74363*pow(10,-4))

def iteration(xi,Es):
    Ea=1000.0
    n=0
    print "Iteration\t\t\txi\t\t\txi_plus\t\t\tEa(%)"
    while(n<Es):
        xi_plus=g(xi)
        if(n!=0):
            Ea=(xi-xi_minus)/xi
            Ea=abs(Ea)*100
        if(n==0):
            print n+1,"\t\t\t",xi,"\t\t\t",xi_plus
        else:
            print n+1,"\t\t\t",xi,"\t\t\t",xi_plus,"\t\t\t",Ea
        n+=1
        xi_minus=xi
        xi=xi_plus

def main():
    xi=float(input("Enter value:"))
    es=input("Enter prespecifid error:")
    iteration(xi,es)

if __name__=="__main__":
    main()
