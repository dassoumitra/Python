#Author - Soumitra Das                                  Date - 05/01/2023
#(h)	Count number of items in the list.

a = [1,2,5,7,5,8,4,1,4,5]
print("Before count the list : ",a)
ele=int(input("Enter the element : "))
co=a.count(4)
print("After count,an item of {} is = {} times".format(ele,co))