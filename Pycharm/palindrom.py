#print("Kamal Kumar Rana")
#n=int(input("Enter a number:: "))
#print(n)
def palindrom(n):
    num=n
    rev=0
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10

    if(rev==num):
        #print(num,"is Palindrom!")
        return 1
    else:
        # print(num,"is not Palindrom!")
        return 0

    
for i in range(1,150):
    if(palindrom(i)):
        print(i)
    