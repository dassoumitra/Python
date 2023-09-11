# Author - Soumitra Das                   Date - 10/02/2023
# 3.write a program to show the prime number in between 1 to 5000.
n=int(input("Enter a number : "))
print("All prime numbers in between 1 to {} are : ".format(n))
for i in range(1,n+1,1):
    count=0
    for j in range (1,i+1,1):
        if(i%j==0):
            count+=1
    if(count==2):
        print(i,end=' ')