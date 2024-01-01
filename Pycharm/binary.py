def binary_search(list, key):
	low = 0
	upper = len(list) - 1
	mid = 0

	while low <= upper:
		mid = (low + upper) // 2

		if list[mid] < key:
			low = mid + 1
		elif list[mid] > key:
			upper = mid - 1
		else:
			return mid

	return -1
		



list=[10,4,5,40,30]
key=40
a=binary_search(list,key)
if a!=-1:
	print("found in location:",a+1)
else:
	print("Not found")