#ask the user to enter the numbers

n1=float(input("Enter the number:"))

operator=input("enter operator:")

n2=float(input("enter number:"))

if (operator=='+'):
    print(n1,operator,n2,'=',n1+n2)
elif(operator=='-'):
    print(n1,operator,n2,'=',n1-n2)
elif(operator=='*'):
    print(n1,operator,n2,'=',n1*n2)
elif(operator=='/'):
    print(n1,operator,n2,'=',n1/n2)
else:
    print("invalid operator")

