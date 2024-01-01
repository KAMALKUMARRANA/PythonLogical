def prime(n):
	flag=0
	for i in range(2,(n//2)+1):
		if n%i==0:
			flag=1
			break
	if flag==0:
		print(n)
	

n=int(input("Enter the total number of element: "))
a=[]
print(f"Enter the {n} elements:: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)
for i in range(0,n):
	prime(a[i])
	

