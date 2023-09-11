#Author - Soumitra Das                              Date - 05/01/2023
#(o) illustrate shallow copy .
import copy
s5= [1,2,[3,4,5],6,[7,8,9,10],11]
print("The original list is :",s5)
s6=copy(s5)
print("The copied list is :",s6)
s5[4][2]=99#add 99 in inner list s5[4][2]
print("The original list is: ",s5)
print("The copied list is :",s6)


