n=input("Enter a string to check: ")
str=""
pos=int(input("Enter position: "))
for i in range(0,len(n)):
	if i!=(pos-1):
		str=str+n[i]
print(str)