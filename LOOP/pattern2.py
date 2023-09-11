# Author - Soumitra Das                   Date - 10/02/2023
# 7.Display the following pattern
# 0
# 1 0 	
# 1 1 0
# 1 1 1 0
r=int(input("Enter row number : "))
print("Pattern is : ")
for i in range(1,r+1,1):
    for j in range(1,i+1,1):
       if(i==j):
        print(0,end=' ')
       else:
        print(1,end=' ')
    print("\n")


