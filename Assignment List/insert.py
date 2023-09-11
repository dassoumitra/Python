#Author - Soumitra Das                                  Date - 05/01/2023
#(e)	Insert an item in the 3rd position of a list.

li = ['python','is','a','language']
print("Before insert an item the list is : ",li)
pos=int(input("Enter the position where can be insert : "))
ele=input("Enter the element : ")
li.insert(pos-1,ele)
print("After insert an item the  list is : ",li)