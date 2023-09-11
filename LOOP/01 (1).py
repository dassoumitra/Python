'''
Python provides the following loops
1) while loop
2) for loop

while loop
==========
A while loop repetitivly executes a target statement or block of 
statements as long as the given condidtion in the expression is true.

syntax
------
while expression:
    statement block

'''
# Program to print all natural number upto 100
# n = 1
# while n <= 5:
#     print(n, end='-')
#     n+=1
'''
end Parameter in print function
------------
The end parameter in the print function is used to add 
any string, at the end of the output of the print statement 
in python. By default, the print function ends with a newline.
'''
# n = 1
# while n <= 100:
#     print(n, end=' ')
#     n+=1

# Program to get sum of the digits of a number
# n=int(input('Enter a number: '))
# s = 0
# while n != 0:
#     r= n%10
#     s+=r
#     n//=10
# print("The sum of the digits: ",s)


'''
in Operator
============
The in operator  (also known as membership operator) is used for 
containment checking in a container. 
The operator returns True or False depending on whether the element 
is present in the container or not.

'''
# print('s' in 'Computer')
# print('e' in 'Hello')
# print(10 in [20,10,60])
# print(1 in (1, 2, 3))
# print(8 in {8, 50, 60, 10})

'''
for Loop
=========
It is suited for the problem where we have prior knowledge of 
the number of times the statement or block will be executed. 

Syntax
------
for var in sequence:
    statement block

'''

# Program to print elements of a list
# list1 = [15, 16, 10 , 8]
# for i in list1:
#     print(i, end=' ')

# Program to print elements of a tuple
# t = (15, 16, 10 , 8)
# for i in t:
#     print(i)

# Program to print elements of a set
# s = {15, 16, 10 , 8}
# for i in s:
#     print(i)

# Program to print Dictionary
# 1. Iterate over keys
# d = {'C':68, 'DS':55, 'Python':87, 'Algo':74, 'CO':68}
# for i in d.keys():  # keys() method returns list of all keys
#     print("Subject: {}, Marks: {}".format(i,d[i]))

# 2. Iterate over Key-Value pair
# d = {'C':68, 'DS':55, 'Python':87, 'Algo':74, 'CO':68}
# for i,j in d.items():  # items() method returns a list of elements (key, value) as tuples
#     print("Subject: {}, Marks: {}".format(i,j))

'''
range() Functon
===============
is used to generate an immutable sequence of numbers.

range(start, stop, step)

start:  an integer value at which the sequence begins; 
        if not specified then it begins a 0.
stop:   is always required and specifies the integer that is 
        counted up to but not included.
step: specifies how much to increase or decrease the next iteration

syntax
------
for var in range(start, stop, step):
    statement block
'''
# print 1 to 10
# for i in range(21):
#     print(i, end=' ')

# print list items using index
# list1 = [10, 20, 30, 40, 50, 60, 70]
# n=len(list1)
# print("Elements in the list at odd positition are: ")
# for i in range(1,n,2):
#     print(list1[i])

'''
Nested Loop
===========
The loop  inside another loop.
'''
# for i in range(3):
#     for j in range(3):
#         print(i, ' ', j)
#     print('I am outside of INNER loop')
# print('I am outside of OUTER loop')

# Program to find common elements of two lists using nested loop
# list1 =[10, 12, 58, 33, 22, 50, 49, 25]
# list2 = [5, 12, 2, 22, 49, 13, 99, 78, 10]
# for i in list1:
#     for j in list2:
#         if i == j:
#             print(i)

'''
Control Statements
==================
- Change the execution of a program from its normal sequence.
    1) exit Function
    2) break Statement
    3) continue Statement
    4) pass Statement

exit Function 
=============
is used to exit and come out of the program.
'''
# for i in range(11):
#     if i == 5:
#         exit()
#     print(i,end=' ')
# print("Execute this Statement.")
# print("Execute this Statement too..")

'''
break Statement
=================
is used to terminate the execution of current loop.
'''
# for i in range(11):
#     if i == 5:
#         break
#     print(i)
# print("Execute this Statement.")
# print("Execute this Statement too..")

# break within while loop
# i=1
# while i<=10:
#     if i==5:
#         break;
#     print(i, end=' ')
#     i+=1
    

# break within nested loop
# for i in range(5):
#     for j in range(5):
#         print(i, ' ', j)
#         if j == 3:
#             break;
#     print('I am outside of INNER loop')
# print('I am outside of OUTER loop')

'''
else Clause in loop
===================
is executed only if the loop terminates normally, 
i.e., terminates through exhaustion of the iterable.
'''
# for i in range(10):
#     print(i)
#     if i == 6:
#         break
# else:
#     print('else clause executed')

'''
continue Statement
==================
- returns the control to the beginning of the current loop.
- causes the loop to skip the remainder of its body
'''
# for i in range(1,11):
#     if i==6:
#         continue
#     print(i, end=' ')

# continue within while loop
# i=1
# while i<=10:
#     # if i==5:
#     #     continue;
#     print(i, end=' ')
#     i+=1

'''
pass Statement
==============
is used when a statement is required syntactically, but
we don't want any code to execute.

It is a null operation.
'''
i=1
while i<=10:
    if i==5:
        pass
    print(i, end=' ')
    i+=1