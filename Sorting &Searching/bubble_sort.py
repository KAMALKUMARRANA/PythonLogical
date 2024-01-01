def bubble_sort(list):
    for i in range(0,len(list)):
        for j in range(1,len(list)-i):
            if list[j-1]>list[j]:
                temp=list[j-1]
                list[j-1]=list[j]
                list[j]=temp
    print(list)
            
            

n=int(input("Enter the total number of element:: "))
a=[]
print(f"Enter {n} elements: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)

bubble_sort(a)

