#Author - Soumitra Das                            Date - 24/01/2023
#2. Write a program (WAP) to print the largest of three numbers.
n1=int(input("Enter a first number :"))
n2=int(input("Enter a second number :"))
n3=int(input("Enter a third number :"))
if n1>n2:
    if n1>n3:
        print("Large number is {}".format(n1))
    else:
        print("Large number is {}".format(n3))
else:
    if n2>n3:
        print("Large number is {}".format(n2))
    else:
        print("Large number is {}".format(n3))