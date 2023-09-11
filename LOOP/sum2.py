#Author - Soumitra Das                         Date - 10/02/2023
# 5.write a program to get the sum of the following example-
#       x+x²/2!+x³/3!+......+x^n/n!
import math
n=int(input("Enter the term : "))
x=int(input("Enter a value of x : "))
sum=0
for i in range(1,n+1,1):
    po=pow(x,i)
    fact=1
    for j in range(1,i+1,1):
        fact=fact*j
    di=po/fact
    sum=sum+di
print("The sum is :",sum)
    



