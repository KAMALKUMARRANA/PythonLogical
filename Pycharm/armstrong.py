print("Kamal Kumar Rana")

def arm(n):
    num=n
    rev=0
    length=len(str(n))
    while(n!=0):
        rem=n%10
        rev=(rev)+(rem**length)
        n=n//10
    


    if(rev==num):
        return 1

    else:
        return 0


n=int(input("Enter a range:: "))
for i in range(1,n+1):
    if arm(i):
        print(i)


    