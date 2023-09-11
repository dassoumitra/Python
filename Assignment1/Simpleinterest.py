#Author - Soumitra Das                                   Date - 15/12/2022
#15. Write a program to enter P, T, R and calculate Simple Interest.
P = int (input("Enter a value of P = "))
R = float (input("Enter a value of R = "))
T = int (input("Enter a value of T = "))
i = float((P*R*T)/100)
print("The simple interest = {}".format(i))