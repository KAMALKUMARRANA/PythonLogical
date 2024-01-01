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


n=int(input("Enter the total number of element:: "))
a=[]
print(f"Enter {n} elements: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)

key=int(input("Enter the searching elements: "))
linear_search(a,key)

