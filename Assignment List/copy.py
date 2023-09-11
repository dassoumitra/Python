#Author - Soumitra Das                                  Date - 05/01/2023
#(k)	Copy the list into another list.

list1 = [4,7,5,8,7,2,4]
print("Before copy , list1 is : ",list1)
list2 =list1.copy()
print("After copy , list2 is : ",list2)
print(id(list1))
print(id(list2))