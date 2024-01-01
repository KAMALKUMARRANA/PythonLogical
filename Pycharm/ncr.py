def fact(num):
	fac=1
	for i in range(1,(num+1)):
		fac=fac*i
	return fac

n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
ncr=fact(n)/(fact(r)*fact(n-r))
print(f"{n}C{r} is: {ncr}")