print("This is Calculator! ")
n1=int(input("Enter the first number: "))
n2=int(input("Enter the second number: "))
op=input("Enter the operator(+,-,*,/,%,**): ")
if(op=="+"):
    print("Addition of ",n1,"and",n2,"is: ",n1+n2)
elif(op=="-"):
    print("Substraction of ",n1,"and",n2,"is: ",n1-n2)
elif(op=="*"):
    print("Multiplication of ",n1,"and",n2,"is: ",n1*n2)
elif(op=="/"):
    print("Division of ",n1,"and",n2,"is: ",n1/n2)
elif(op=="%"):
    print("Modulo division of ",n1,"and",n2,"is: ",n1%n2)
elif(op=="**"):
    print(n1,"to the power",n2,"is: ",n1**n2)
else:
    print("Operation is not available!")