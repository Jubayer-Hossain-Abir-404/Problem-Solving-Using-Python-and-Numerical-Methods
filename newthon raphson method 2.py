def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993
def f_prime(x):
    return 3*pow(x,2)-0.165*2*x


def newton(a,i):
    print "Iteration\t\txi\t\txi1\t\tEa(%)"
    n=0
    xi=a
    while(n<i):
        xi1=xi-(f(xi)/f_prime(xi))
        Ea=(xi1-xi)/xi1
        if(Ea<0):
            Ea*=-1
        Ea*=100
        print n+1,"\t\t",xi,"\t\t",xi1,"\t\t",Ea
        xi=xi1
        n+=1

def main():
    newton(0.05,4)


if __name__ =="__main__":
    main()
