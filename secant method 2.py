def f(x):
    return pow(x,3)-0.165*x*x+0.0003993
def secant(xi,xi_minus,Es):
    Ea=200.0
    while(Ea>Es):
        xi_plus=xi-(f(xi)*(xi-xi_minus))/(f(xi)-f(xi_minus))
        Ea=(xi_plus-xi)/xi_plus
        Ea=abs(Ea)
        Ea*=100
        xi_minus=xi
        xi=xi_plus

    print "The root is:",xi_plus


def main():
    xi=input("Enter Upper Boundary:")
    xi_minus=input("Enter Lower Boundary:")
    Es=input("Input Error Tolarance:")
    secant(xi,xi_minus,Es)


if __name__=="__main__":
    main()
