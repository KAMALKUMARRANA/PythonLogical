print("Kamal Kumar Rana")
n=int(input("Enter a number:: "))
print(n)
num=n
rev=0
while(n!=0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10

if(rev==num):
    print(num,"is Palindrom!")
else:
    print(num,"is not Palindrom!")
    