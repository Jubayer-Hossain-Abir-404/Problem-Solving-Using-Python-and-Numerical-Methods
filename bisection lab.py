def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993

def bisection(a,b,Es):
    if(f(a)*f(b)<0):
        print "Iteration\t\t\txl\t\t\txu\t\t\txm\t\t\tEa"
        n=0
        Ea=1000.0
        while(Ea>Es):
            xl=a
            xu=b
            xm=(a+b)/2.0
            if(f(a)*f(xm)<0):
                b=xm
            elif(f(a)*f(xm)>0):
                a=xm
            else:
                print "The root is ",xm
                break
            if(n!=0):
                Ea=(xm-xmold)/xm
                Ea=abs(Ea)*100
            if(n==0):
                print n+1,"\t\t\t",xl,"\t\t\t",xu,"\t\t\t",xm
            else:
                print n+1,"\t\t\t",xl,"\t\t\t",xu,"\t\t\t",xm,"\t\t\t",Ea
            xmold=xm
            n+=1
    else:
        print "The root does not exist"


def main():
    xl=input("Ener the lower interval:")
    xu=input("Enter the upper interval:")
    es=input("Enter the prespecified error:")
    bisection(xl,xu,es)
if __name__=="__main__":
    main()
