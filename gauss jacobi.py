def f1(y,z):
    return (7-2*y+z)/10

def f2(x,z):
    return (-4-x-z)/8

def f3(x,y):
    return (9+2*x+y)/10


def gauss_jacob(x,y,z,n):
    print "Iteration\t\tx1\t\tx2\t\tx3\t\tEa"
    for i in range(0,n):
        xold=x
        yold=y
        zold=z
        x=f1(yold,zold)
        y=f2(xold,zold)
        z=f3(xold,yold)
        Eax=abs(((x-xold)/x)*100)
        Eay=abs(((y-yold)/y)*100)
        Eaz=abs(((z-zold)/z)*100)
        if(Eax>Eay):
            if(Eax>Eaz):
                Ea=Eax
            else:
               Ea=Eaz
        if(Eay>Eax):
            if(Eay>Eaz):
                Ea=Eay
            else:
                Ea=Eaz
        if(Eax==Eay):
            if(Eay==Eaz):
                Ea=Eax
            elif(Eay<Eaz):
                Ea=Eaz
            else:
                Ea=Eax
        print i+1,"\t\t",xold,"\t\t",yold,"\t\t",zold,"\t\t",Ea

def main():
    n=input("How many iterations do you want to take:")
    gauss_jacob(0.0,0.0,0.0,n)

if __name__=="__main__":
    main()
        
        
        
