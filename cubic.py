def cubic(x,y,x1):
	n=0
	b0=y[n]
	b1=(y[n+1]-y[n])/(x[n+1]-x[n])
	b2=(((y[n+2]-y[n+1])/(x[n+2]-x[n+1]))-((y[n+1]-y[n])/(x[n+1]-x[n])))/(x[n+2]-x[n])
	bm=(((y[n+3]-y[n+2])/(x[n+3]-x[n+2]))-((y[n+2]-y[n+1])/(x[n+2]-x[n+1])))/(x[n+3]-x[n+1])
	b3=(bm-b2)/(x[n+3]-x[n])
	ans=b0+b1*(x1-x[n])+b2*(x1-x[n])*(x1-x[n+1])+b3*(x1-x[n])*(x1-x[n+1])*(x1-x[n+2])
	print ans
	



def main():
	x=[0.0]*(3+1)
	y=[0.0]*(3+1)
	for i in range(0,3+1):
		x[i]=input("Input the value of x:")
	for i in range(0,3+1):
		y[i]=input("Input the value of y:")
	x1=input("Determine the value:")
	cubic(x,y,x1)
if __name__=="__main__":
	main()
