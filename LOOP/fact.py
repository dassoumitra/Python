# Author - Soumitra Das                   Date - 10/02/2023
# 2.Write a program to find the factorial of a given number.
n=int(input("Enter a number : "))
fact=1
for i in range(1,n+1,1):
    fact=fact*i
print("The factorial of {} is : {} ".format(n,fact))