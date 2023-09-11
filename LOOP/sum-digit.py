# Author - Soumitra Das                   Date - 10/02/2023
#1.Write a program to calculate the sum of the digits of a number
n=int(input("Enter a number : "))
sum=0
c=n
while(n>0):
    r=n%10
    sum+=r
    n//=10
print("The sum of the digits of {} is : {}".format(c,sum))



