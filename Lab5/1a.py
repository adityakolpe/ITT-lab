#!usr/bin/python
a=int(input("Enter a: "))
o=input("Enter operation (+, -, *, /): ")
b=int(input("Enter b: "))

if (o=='+'):
    print ("a + b =",a+b)
elif (o=='-'):
    print ("a - b =",a-b)
elif (o=='*'):
    print ("a * b =",a*b)
elif (o=='/'):
    print ("a / b =",a/b)
