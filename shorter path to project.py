import math
def g(x):
    return (-0.88318*pow(10,-2))/(-0.50598*pow(10,-10)*pow(x,2)+0.38292*pow(10,-7)*x+0.74363*pow(10,-4))
def iteration(xi):
    n=0
    while(n<5):
        xi_plus=g(xi)
        n+=1
        xi=xi_plus
    return xi
def calculate(n,T,alpha):
    sum_Ti=0.0
    sum_Ti_square=0.0
    sum_Ti_cube=0.0
    sum_Ti_four=0.0
    sum_ai=0.0
    sum_aiTi=0.0
    sum_ai2=0.0
    for i in range(0,7):
        sum_Ti=sum_Ti+T[i]
        sum_Ti_square=sum_Ti_square+pow(T[i],2)
        sum_Ti_cube=sum_Ti_cube+pow(T[i],3)
        sum_Ti_four=sum_Ti_four+pow(T[i],4)
        sum_ai=sum_ai+alpha[i]
        sum_aiTi=sum_aiTi+(alpha[i]*T[i])
        sum_ai2=sum_ai2+(alpha[i]*(T[i]*T[i]))
    a=[0.0]*3
    for i in range(0,3):
        a[i]=[0.0]*3
    b=[0.0]*3
    p=3
    for i in range(0,p):
        for j in range(0,p):
            if(i+j==0):
                a[i][j]=n
            elif(i+j==1):
                a[i][j]=sum_Ti
            elif(i+j==2):
                a[i][j]=sum_Ti_square
            elif(i+j==3):
                a[i][j]=sum_Ti_cube
            elif(i+j==4):
                a[i][j]=sum_Ti_four
    for i in range(0,p):
        if(i==0):
            b[i]=sum_ai
        elif(i==1):
            b[i]=sum_aiTi
        elif(i==2):
            b[i]=sum_ai2
    for i in range(0,p-1):
        for j in range(i+1,p):
            factor=a[j][i]/a[i][i]
            for k in range(i+1,p):
                a[j][k]=a[j][k]-factor*a[i][k]
            b[j]=b[j]-factor*b[i]
    x=[0.0]*3
    x[p-1]=b[p-1]/a[p-1][p-1]
    i=p-2
    while(i>=0):
        value=b[i]
        for j in range(i+1,p):
            value=value-a[i][j]*x[j]
        x[i]=value/a[i][i]
        i=i-1
    Tf=iteration(0)
    print Tf, "temperature is needed to cool the trunion in order to get the desired contraction\n"
    print "So,-108 degree farenheit is not going to work to contract the trunion\n"
def main():
    T=[80.0,40.0,-40.0,-120.0,-200.0,-280.0,-340.0]
    alpha=[0.00000647,0.00000624,0.00000572,0.00000509,0.00000430,0.00000333,0.00000245]
    calculate(7.0,T,alpha)
if __name__=="__main__":
    main()
