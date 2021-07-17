def regression(x,y,n):
    sum_x=0.0
    sum_y=0.0
    sum_xy=0.0
    sum_x_square=0.0
    for i in range(0,7):
        sum_x+=x[i]
        sum_y+=y[i]
        sum_xy+=x[i]*y[i]
        sum_x_square+=x[i]*x[i]
    x_mean=sum_x/n
    y_mean=sum_y/n
    a1=((n*sum_xy)-(sum_x*sum_y))/((n*sum_x_square)-(sum_x*sum_x))
    a0=y_mean-a1*x_mean
    print "a1:",a1
    print "a0:",a0
    print "y=",a0,"+",a1,"*x"
    
def main():
    x=[1726,1542,2816,5555,1292,2208,1303]
    y=[3681,3395,6653,9543,3318,5563,3760]
    n=7.0
    regression(x,y,n)

if __name__=="__main__":
    main()
