def g(x):
    return (x+(5/x))/2.0

def iteration(xi,Es):
    Ea=1000.0
    n=0
    while(Ea>Es):
        xi_plus=g(xi)
        if(n!=0):
            Ea=(xi-xi_minus)/xi
            Ea=abs(Ea)
            Ea*=100
        xi_minus=xi
        xi=xi_plus
        n=n+1

    print "The root is:",xi_plus


def main():
    xi=input("Input a value:")
    Es=input("Input Error Tolarance:")
    iteration(xi,Es)


if __name__=="__main__":
    main()
        
