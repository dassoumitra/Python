#Author - Soumitra Das                                  Date - 05/01/2023
#(m) illustrate join() and split() method.

li = ['python','is','a','object','oriented','language']
stg = '*'
print("Before join method , list is : ",li)
stg = stg.join(li)
print("After join method , list is : ",stg)

msg = "I Love My Parents"
print("Before split: ",msg)
li = msg.split()
print("After split, list is : ",li)
