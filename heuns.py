import math
def temp(th):
	return (-2.2067*pow(10,-12))*(pow(th,4)-81*pow(10,8))

def heuns(h,t):
    y1=0
    t1=0
    y=1200.00
    while(t>t1):
        k1=temp(y)
        k2=temp(y+k1*h)
        y1=y+(0.5*k1+0.5*k2)*h
        print "Result:",y1
        y=y1
        t1=t1+h
		


def main():
	h=input("Input the valyue of step size:")
	t=480
	heuns(h,t)

if __name__=="__main__":
	main()
