def g(x):
    return (x+5/x)/2.0


def iteration(xi,i):
    n=0
    while(n<i+1):
        xi_plus=g(xi)
        if(n!=0):
            Ea=(xi-xi_minus)/xi
            Ea=abs(Ea)
            Ea*=100
            print "The absolute realtive approximate error:",Ea
        xi_minus=xi
        xi=xi_plus
        n=n+1

    print "The root is:",xi_plus


def main():
    xi=input("Input a value:")
    i=input("Input the number of iteration:")
    iteration(xi,i)


if __name__=="__main__":
    main()
