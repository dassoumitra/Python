# Author - Soumitra Das                   Date - 10/02/2023
# 6.Display the following pattern
#   1
#   2 3 
#   4 5 6
#   7 8 9 10
r=int(input("Enter row number : "))
count=1
print("Pattern is : ")
for i in range(1,r+1,1):
    for j in range(1,i+1,1):
        print(count,end=' ')
        count+=1
    print("\n")
# for i in range(1,r+1,1):
