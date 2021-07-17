import math
def f(x):
	a=140000/float(140000-(2100*x))
	return 2000*(math.log(a))-(9.8*x)

def trapezoid(a,b,n):
	tramp=0
	h=(b-a)/float(n)
	if(n==1):
		tramp=tramp+((b-a)/2*n)*(f(a)+f(b))
	elif(n>1):
		tramp=f(a)
		for i in range(1,n):
			tramp=tramp+2*f(a+i*h)
		tramp=tramp+f(b)
		tramp=((b-a)/float(2*n))*tramp
	Et=11061.34-tramp
	Etabs=abs(((11061.34-tramp)/11061.34)*100)
	print "x:11061.34"
	print "I:",tramp
	print "\nn:",n," I:",tramp," Et:",Et," Et(%):",Etabs


def main():
	n=input("Input the number of segment:")
	trapezoid(8,30,n)

if __name__=="__main__":
	main()

