# Sets
# ======
# (a) Create an empty set
# (b) add some elements to it
# (c) prove that set elements are unique
# (d) create sets from list, tuple and string
# (e) use update() method to update a set
# (f) create a frozen set
# (g) use union and intersection method to do operations on sets
# (h) copy a set

#Author - Soumitra Das                       Date - 10/01/2023
# # (a) Create an empty set
# set1=set()
# print("The empty set is : ",set1)

# ## #Author - Soumitra Das                       Date - 10/01/2023
# # (b) add some elements to it
set1=set()
print("The set is : ",set1)
set1.update({1,4,85,3})
print("After add some elements , the set is :",set1)

#Author - Soumitra Das                       Date - 10/01/2023
# # (c) prove that set elements are unique
# s2={1,1,1,2,2,4,5,6,3,3,4,3}
# print("The set is : ",s2)
# print("Set don't print the duplicate value, So set elements are unique.")
##

## #Author - Soumitra Das                       Date - 10/01/2023
# # (d) create sets from list, tuple and string
# li=[1,4,562,4,2,5,3]
# print("The list is",li)
# tu=(7,8,5,7,2,4,2)
# print("The tuple is",tu)
# st="Central Calcutta Polytechnic"
# print("The string is",st)
# print("The set from the list : ")
# print(set(li))
# print("The set from the tuple : ")
# print(set(tu))
# print("The set from the string : ")
# print(set(st))


## #Author - Soumitra Das                       Date - 10/01/2023
# (e) use update() method to update a set
# set1={1,2,3,4,5,2,1}
# set2={7,8,9,4,5,2}
# print("The first set is :",set1)
# print("The second set is :",set2)
# print("After update() method , the set is : ",end=' ')
# set1.update(set2)
# print(set1)

## #Author - Soumitra Das                       Date - 10/01/2023
# (f) create a frozen set
# fs={1,1,2,4,3,5,2}
# print("The frozenset is :",end='')
# print(frozenset(fs))

## #Author - Soumitra Das                       Date - 10/01/2023
# # # (g) use union and intersection method to do operations on sets
# s3={1,2,3,4,5,6}
# s4={5,6,7,8}
# print("The first set is : ",s3)
# print("The second set is : ",s4)
# print("After union() method the  set is : ")
# print(s3.union(s4))
# print("After intersection() method the  set is : ")
# print(s3.intersection(s4))

## #Author - Soumitra Das                       Date - 10/01/2023
# # (h) copy a set
# import copy
# s5={1,2,3,4,5}
# print("The original set is :",s5)
# s6=copy.deepcopy(s5)
# print("The copied set is :",s6)
# print("The id of original set is :",id(s5))
# print("The id of copied set is :",id(s6))