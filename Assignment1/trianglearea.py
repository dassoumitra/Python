#Author - Soumitra Das                               Date - 15/12/2022
#12. Write a program to enter base and height of a triangle and find its area.
b = int (input("Enter a value of base of triangle : "))
h = int (input("Enter a value of height of triangle : "))
area = float(1/2*b*h)
print("The area of a triangle is = {}".format(area))