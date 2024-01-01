
def fun(num):
    flag=0
    if num >1:
        for i in range(2,((num//2)+1)):
            if  num%i==0:
                    flag=1
        if flag==0:
            return 1
        else:
            return 0

n1=int(input("Enter the starting range: "))  
n2=int(input("Enter the ending range: "))
for i in range(n1,n2):
    if fun(i):
        print(i)
            
        