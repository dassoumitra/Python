#Author - Soumitra Das                                  Date - 05/01/2023
#(n) create list alias.

a = [1,4,5,7,3,2]
b = a
print("List 'a' is :",a)
print("List 'b' is :",b)
if (id(a)==id(b)):
    print("Alias is occured")
else:
    print("Not occured")