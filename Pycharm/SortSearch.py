def bubble_sort(a):
	for i in range(len(a)):
		for j in range(1,len(a)-i):
			if a[j-1]>a[j]:
				temp=a[j-1]
				a[j-1]=a[j]
				a[j]=temp
	print(a)
	

def selection_sort(a):
	for i in range(len(a)):
		min_index=i
		for j in range(i+1,len(a)):
			if a[min_index]>a[j]:
				min_index=j
		(a[min_index],a[i])=(a[i],a[min_index])
	print(a)
			

def insertion_sort(a):
	for i in range(1,len(a)):
		temp=a[i]
		j=i-1
		while j>=0 and temp<a[j]:
			a[j+1]=a[j]
			j=j-1
		a[j+1]=temp

	print(a)
		
		
def binary(a,key):
	l=0
	u=len(a)-1
	m=0
	while l<=u:
		mid=(l+u)//2
		if a[mid]<key:
			l=mid+1
		elif a[mid]>key:
			u=mid-1
		else:
			return mid
	return -1
	

def linear_search(a,key):
	flag=0
    for i in range(0,len(a)):
        if key==a[i]:
            flag=1
            break
    if flag==1:
        print(key,"in location:",i+1)
    else:
         print(key,"is not found!")

