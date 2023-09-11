#Author - Soumitra Das                                  Date - 05/01/2023
#(g)	Find the index of a given item by using index() method.

a = [5,8,4,2,1]
print("List is : ")
print(a)
ele=int(input("Enter the element from above list : "))
ind=a.index(ele)
print("Index of {} is : {}".format(ele,ind))
