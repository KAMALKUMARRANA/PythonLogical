def avg(a):
    sum=0
    for i in a:
        sum=sum+i
        i=i+1
    print("Average of list elements: ",(sum/len(a)))
    



n=int(input("Enter the total number of element: "))
a=[]
print(f"Enter the {n} elements:: ")
for i in range(0,n):
    e=int(input())
    a.append(e)
print(a)
avg(a)

    
    