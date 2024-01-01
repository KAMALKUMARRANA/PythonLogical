def fact(num):
	fac=1
	for i in range(1,(num+1)):
		fac=fac*i
	return fac

n=int(input("Enter the value of n: "))
r=int(input("Enter the value of r: "))
npr=fact(n)/(fact(n-r))
print(f"{n}P{r} is: {npr}")