import math
def f(x):
	a=140000/float(140000-(2100*x))
	return 2000*(math.log(a))-(9.8*x)

def simpson(a,b,n):
	h=(b-a)/float(n)
	tramp=f(a)+f(b)
	for i in range(1,n):
			if(i%2!=0):
				tramp=tramp+4*f(a+i*h)
	for i in range(2,n-1):
			if(i%2==0):
				tramp=tramp+2*f(a+i*h)
	tramp=(((b-a)/float(3*n))*tramp)
	Et=11061.34-tramp
	Etabs=abs(((11061.34-tramp)/11061.34)*100)
	print "x:11061.34"
	print "I:",tramp
	print "\nn:",n," I:",tramp," Et:",Et," Et(%):",Etabs


def main():
	n=input("Input the number of segment:")
	simpson(8,30,n)

if __name__=="__main__":
	main()

