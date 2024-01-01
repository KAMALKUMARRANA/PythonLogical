n=input("Enter a string to check: ")
rev_str=n[-1::-1]
print(rev_str)
if n==rev_str:
	print(n,"is palindrom string")
else:
	print(n,"is not palindrom string")
 
 
for i in range(len(n)-1,-1,-1):
    print(n[i],end=" ")
     