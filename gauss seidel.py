def f1(x2,x3):
    return (0.1*x2+0.2*x3+7.85)/3

def f2(x1,x3):
    return (-19.3-0.1*x1+0.3*x3)/7

def f3(x1,x2):
    return (71.4-0.3*x1+0.2*x2)/10


def gauss_seidel(x1,x2,x3,n):
    print "Iteration\t\tx1\t\tx2\t\tx3\t\tEa"
    for i in range(0,n):
        x1old=x1
        x2old=x2
        x3old=x3
        x1=f1(x2,x3)
        x2=f2(x1,x3)
        x3=f3(x1,x2)
        Eax1=abs(((x1-x1old)/x1)*100)
        Eax2=abs(((x2-x2old)/x2)*100)
        Eax3=abs(((x3-x3old)/x3)*100)
        if(Eax1>Eax2):
            if(Eax1>Eax3):
                Ea=Eax1
            else:
               Ea=Eax3
        if(Eax2>Eax1):
            if(Eax2>Eax3):
                Ea=Eax2
            else:
                Ea=Eax3
        if(Eax1==Eax2):
            if(Eax2==Eax3):
                Ea=Eax1
            elif(Eax2<Eax3):
                Ea=Eax3
            else:
                Ea=Eax1
        print i+1,"\t\t",x1old,"\t\t",x2old,"\t\t",x3old,"\t\t",Ea

def main():
    n=input("How many iterations do you want to take:")
    gauss_seidel(0.0,0.0,0.0,n)

if __name__=="__main__":
    main()
        
        
        
