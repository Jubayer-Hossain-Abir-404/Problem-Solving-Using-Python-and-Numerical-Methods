def lagrange(x,y,n,x1):
    m=0
    for i in range(0,6-n):
        if(n==1):
            if(x1>=x[i]):
                if(x1<=x[i+1]):
                    m=i
                    break
        if(n==2):
            if(x1>=x[i]):
                if(x1>=x[i+1]):
                    if(x1<=x[i+2]):
                        m=i
                        break
        if(n==3):
            if(x1>=x[i]):
                if(x1>=x[i+1]):
                    if(x1>=x[i+2]):
                        if(x1<=x[i+3]):
                            m=i
                            break
        if(n==4):
            if(x1>=x[i]):
                if(x1>=x[i+1]):
                    if(x1>=x[i+2]):
                        if(x1>=x[i+3]):
                            if(x1<=x[i+4]):
                                m=i
                                break
        if(n==5):
            if(x1>=x[i]):
                if(x1>=x[i+1]):
                    if(x1>=x[i+2]):
                        if(x1>=x[i+3]):
                            if(x1>=x[i+4]):
                                if(x1<=x[i+5]):
                                    m=i
                                    break
    p=m+1
    p=p+n
    sum=0.0
    Lt=1
    for i in range(m,p):
        for j in range(m,p):
            if(j!=i):
                Lt=Lt*((x1-x[j])/(x[i]-x[j]))
        sum=sum+Lt*y[i]
        Lt=1


    print "The result is:",sum
            
        
def main():
    x=[0,10.0,15.0,20.0,22.5,30.0]
    y=[0,227.04,362.78,517.35,602.97,901.67]
    n=input("Input the value of n:")
    x1=input("Determine the value:")
    lagrange(x,y,n,x1)




if __name__=="__main__":
    main()
