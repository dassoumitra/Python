#Author - Soumitra Das                                   Date - 15/12/2022
#11. Write a program to enter two angles of a triangle and find the third angle.
a1 = int (input("Enter a first angle of triangle : "))
a2 = int (input("Enter a second angle of a triangle : "))
a3 = 180 - (a1+a2)
print("The third angle of triangle is : {}".format(a3))