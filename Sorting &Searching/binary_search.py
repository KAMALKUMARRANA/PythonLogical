def binary_search(list,key):
    low=0
    upper=len(list)-1
    mid=0

    while low<=upper:
        mid=(low+upper)//2

        if list[mid]<key:
            low=mid+1
        elif list[mid]>key:
            upper=mid-1
        else:
            return mid
            
    return -1

n=int(input("Enter the total number of elements in list:"))
a=[]
print(f"Enter The {n} elements in the list: ")

for i in range(0,n):
    e=int(input())
    a.append(e)
print("The list is:",a)
key=int(input("Enter the searching Elements:"))
res=binary_search(a,key)
if res!=-1:
    print(key," is  found in the list at the location:",res+1)
    
else:
    print(key," is not found in the list!")