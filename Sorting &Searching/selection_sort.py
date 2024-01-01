def selection_sort(list):
	
	for i in range(len(list)):
		min_index=i
		for j in range(i+1,len(list)):
			if list[min_index]>list[j]:
				min_index=j
		# (a[i],a[min_index])=(a[min_index],a[i])
		temp=list[i]
		list[i]=list[min_index]
		list[min_index]=temp
	print(list)
			



n=int(input("Enter the total number of element: "))
print("Enter elements: ")
a=[]
for i in range(n):
    e=int(input())
    a.append(e)
print(a)

selection_sort(a)