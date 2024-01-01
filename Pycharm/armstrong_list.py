def armstrong(n):
	sum=0
	num=n
	while n!=0:
		rem=n%10
		sum=sum+rem**len(str(num))
		n=n//10
	if num==sum:
		print(num,end=" ")
	

n=int(input("Enter the total number of element: "))
a=[]
print(f"Enter the {n} elements:: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)
for i in range(0,n):
	armstrong(a[i])
	