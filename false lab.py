def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993

def false(a,b,Es):
    if(f(a)*f(b)<0):
        n=0
        Ea=1000.0
        print "Iteration\t\t\txl\t\t\txu\t\t\txm\t\t\tEa(%)"
        while(Ea>Es):
            xl=a
            xu=b
            xm=b-(f(b)*(a-b))/(f(a)-f(b))
            if(f(a)*f(xm)<0):
                b=xm
            elif(f(a)*f(xm)>0):
                a=xm
            else:
                print "The root is ",xm
            if(n!=0):
                Ea=(xm-xmold)/xm
                Ea=abs(Ea)*100
            if(n==0):
                print n+1,"\t\t\t",xl,"\t\t\t",xu,"\t\t\t",xm
            else:
                print n+1,"\t\t\t",xl,"\t\t\t",xu,"\t\t\t",xm,"\t\t\t",Ea
            n+=1
            xmold=xm
    else:
        print "The root does not exist"

def main():
    xl=input("Enter the lower interval:")
    xu=input("Enter the upper interval:")
    es=input("Enter the presepecified error:")
    false(xl,xu,es)

if __name__=="__main__":
    main()
