#Author - Soumitra Das                       Date - 10/01/2023
#(c)	Find the index of a particular item
t = (4,8,6,7,5,7)
print("The tuple is : {}".format(t))
n=int(input("Enter an item from the tuple :"))
print("The index of particular item, {} is :".format(n),end=' ')
print(t.index(n))