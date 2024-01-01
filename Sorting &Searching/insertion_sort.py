def insertion_sort(list):
	for i in range(1,len(list)):
		temp=a[i]
		j=i-1
		while j>=0 and temp<a[j]:
			a[j+1]=a[j]
			j=j-1
		a[j+1]=temp
	print(a)

n=int(input("Enter the total number of element:: "))
a=[]
print(f"Enter {n} elements: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)

insertion_sort(a)
