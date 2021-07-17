def f(x):
    return pow(x,3)-0.165*pow(x,2)+0.0003993
def bisection(a,b,i):
    if(f(a)*f(b)<0):
        n=0
        Ea=0.0
        c=0
        print "Iteration\t\txl\t\txu\t\txm\t\tEa(%)"
        while(n<i):
            xm=(a+b)/2.0
            xl=a
            xu=b
            if(f(a)*f(xm)<0):
                b=xm
            elif(f(a)*f(xm)>0):
                a=xm
            else:
                print "The root is ",xm
                c+=1
                break
            if(c!=1):
                if(n!=0):
                    Ea=(xm-xmold)/xm
                    if(Ea<0):
                        Ea*=-1
                    Ea*=100
                if(n==0):
                    print n+1,"\t\t",xl,"\t\t",xu,"\t\t",xm
                else:
                    print n+1,"\t\t",xl,"\t\t",xu,"\t\t",xm,"\t\t",Ea
            xmold=xm
            n+=1
    else:
        print "The root does not exist"



bisection(0,0.11,4)
                
                
