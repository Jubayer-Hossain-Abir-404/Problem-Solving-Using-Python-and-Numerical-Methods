import math
def f(x):
    return math.exp(-x)-x
def f_prime(x):
    return -math.exp(-x)-1

def newton(xi,Es):
    n=0
    Ea=1000.0
    print "Iteration\t\t\txi\t\t\txi1\t\t\tEa(%)"
    while(Ea>Es):
        xi1=xi-(f(xi)/f_prime(xi))
        Ea=(xi1-xi)/xi1
        Ea=abs(Ea)*100
        print n+1,"\t\t\t",xi,"\t\t\t",xi1,"\t\t\t",Ea
        n+=1
        xi=xi1

def main():
    xi=input("Enter the value:")
    es=input("Enter the prespecified error:")
    newton(xi,es)

if __name__=="__main__":
    main()
