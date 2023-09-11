# Tuples
# =======
# Perform the following operations in a tuple:
# (a)	Create a tuple
# (b)	Concatenate two tuples
# (c)	Find the index of a particular item
# (d)	Find the frequency of a particular item
# (e)	Find the length of the tuple
# (f)	Get maximum and minimum item from the tuple


## (a)	Create a tuple
t1 =(1,5,7,8,4)
print(t1)
t2=('ami','tumi',5,9,[8,5])
print(t2)

# (b)	Concatenate two tuples

t3=(1,2,3)
t4=(4,5,6)
print(t3+t4)


# (c)	Find the index of a particular item


t5=(84,65,56,53,9,9)
print(t5.index(9))
print(t5.index(9))


# (d)	Find the frequency of a particular item

t6=(1,4,6,8,6,6,4,8,5)
b=t6.count(6)
print(b)
print(t6.count(4));print(t6.count(5))


# (e)	Find the length of the tuple

t7=(4,5,7,9)
a=len(t7)
print(a)

# (f)	Get maximum and minimum item from the tuple

t8=(1,2,3,4,5,6)
print(max(t8))
print(min(t8))
list1=[4,4,26,7,89,5]
print(list1[::-1])
