# Dictionary
# =========
# (a)	Create a Dictionary
# (b)	Access Values using Keys
# (c)	Use get() method to access values
# (d)	Create a dictionary from two lists.
# (e)	Add a new item to the dictionary
# (f)	Delete an item
# (g)	Create a nested dictionary
# (h)	Delete an item using pop() method
# (i)	Delete an item using popitem() method
# (j)	Delete all items from a dictionary
# (k)	Get the length of a dictionary
# (l)	Execute items() method
# (m) Create a list with the keys of a dictionary
# (n)	Create a list with the values of a dictionary
# (o)	Update a dictionary items with the items of another dictionary


# #Author - Soumitra Das                       Date - 10/01/2023
# # (a)	Create a Dictionary
# d1={1:'ami',2:'tumi',3:'se',4:'friend'}
# print("The Dictionary is : " ,end=' ')
# print(d1)

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (b)	Access Values using Keys
# d2={1:5,2:4,3:5,3:8}
# print("The Dictionary is {}" .format(d2))
# n=int(input("Enter 'key' from the Dictionary :"))
# print("The value of '{}' is : ".format(n),end=' ')
# print(d2[n])

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (c)	Use get() method to access values
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is : ",d2)
# print(d2.get(2))

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (d)	Create a dictionary from two lists.
# key=['cpu','ssd','ram']
# valu=['2.4Hz','512',8]
# print("The 1st list is : {}".format(key))
# print("The 2st list is : {}".format(valu))
# print("The Dictionary is : ",end=' ')
# print(dict(zip(key,valu)))

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (e)	Add a new item to the dictionary
# d2={1:5,2:4,4:5,3:8}
# print("Before add a new item , The dictionary is: {}".format(d2))
# d2[5]=10
# print("After add a new item , the dictionary is: ",end=' ')
# print(d2)

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (f)	Delete an item
# d2={1:5,2:4,4:5,3:8}
# print("Before delete an item , the dictionary is: {} ".format(d2))
# print("After delete an item , the dictionary is :",end=' ')
# del d2[2]
# print(d2)

# ## #Author - Soumitra Das                       Date - 10/01/2023
# # (g)	Create a nested dictionary
# d1={'c':['dec c++','turbo c'],'python':{64:'vscode',32:'pychram'}}
# print("The nested dictionary is : ",d1)

# # ## #Author - Soumitra Das                       Date - 10/01/2023
# # (h)	Delete an item using pop() method
# d2={1:5,2:4,4:5,3:8}
# print("Before delete an item , the dictionary is: {} ".format(d2))
# a=d2.pop(2)
# print("After delete an item , the dictionary is :",end=' ')
# print(d2)


# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (i)	Delete an item using popitem() method
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is :{} ".format(d2))
# print("After execute 'popitem()' method , the dictionary is: ",end=' ')
# n=(d2.popitem())
# print(d2)


# #Author - Soumitra Das                       Date - 10/01/2023
# # (j)	Delete all items from a dictionary
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is : {} ".format(d2))
# print("After delete all items from a dictionary , the dictionary is : ",end=' ')
# print(d2.clear())

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (k)	Get the length of a dictionary
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is : {} ".format(d2))
# print("The length of dictionary is : ",end=' ')
# print(len(d2))

# #Author - Soumitra Das                       Date - 10/01/2023
# # (l)	Execute items() method
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is : {} ".format(d2))
# print("After excute '.items()' method , the dictionary is : ",end=' ')
# print(list(d2.items()))

# # #Author - Soumitra Das                       Date - 10/01/2023
# # # (m) Create a list with the keys of a dictionary
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is : {} ".format(d2))
# print("A list with the keys of a dictionary is : ",end=' ')
# print(list(d2.keys()))

# #Author - Soumitra Das                       Date - 10/01/2023
# # (n)	Create a list with the values of a dictionary
# d2={1:5,2:4,4:5,3:8}
# print("The dictionary is {} ".format(d2))
# print("A list with the 'values' of a dictionary is : ",end=' ')
# print(list(d2.values()))

# #Author - Soumitra Das                       Date - 10/01/2023
# # (o)	Update a dictionary items with the items of another dictionary
# d1={'a':'ami','b':'baba','c':'maa'}
# d2={'a':'dada','x':'mama'}
# print("The 1st dictionary is ",d1)
# print("The 2nd dictionary is ",d2)
# d1.update(d2)
# print("After update() method , the dictionary is :",d1)