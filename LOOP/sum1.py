# Author - Soumitra Das                   Date - 10/02/2023
# 4.write a program to following example-
#       5+55+555+...........+ upto nth term.
n=int(input("Enter the term : "))
c=n
sum=0
for i in range(1,n+1,1):
    print(n,end='+')
    sum=sum+n
    n=n*10+c
print("\nThe sum of the following pattern is : ",sum)