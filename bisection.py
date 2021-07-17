def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993
def bisection(a,b,i):
    n=0
    if(f(a)*f(b)<0):
        print "\t\tIteration\t\t\t\txl\t\t\t\txu\t\t\txm\t\t\tEa(%)"
        Ea=0.0
        while(n<i):
            xm=(a+b)/2.0
            xl=a
            xu=b
            if(f(a)*f(xm)<0):
                b=xm
            elif(f(a)*f(xm)>0):
                a=xm
            else:
                print "The root is :",xm
                break
            if(n!=0):
                Ea=(xm-xmold)/xm
                if(Ea<0):
                    Ea*=-1
                Ea*=100
            if(n==0):
                print "\t\t",n+1,"\t\t\t",xl,"\t\t\t\t",xu,"\t\t\t\t",xm
            else:
                print "\t\t",n+1,"\t\t\t",xl,"\t\t\t\t",xu,"\t\t\t\t",xm,"\t\t\t",Ea
            xmold=xm
            n+=1
    else:
        print "The root does not exist"


bisection(0,0.11,4)
