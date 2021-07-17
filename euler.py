import math
def temp(th):
	return (-2.2067*pow(10,-12))*(pow(th,4)-81*pow(10,8))


def euler(h,t):
	y1=0
	t1=0
	y=1200.00
	while(t>t1):
		y1=y+temp(y)*h
		print "Result:",y1
		y=y1
		t1=t1+h
		


def main():
	h=input("Input the valyue of step size:")
	t=480
	euler(h,t)

if __name__=="__main__":
	main()
