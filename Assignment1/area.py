#Author - Soumitra Das                               Date - 15/12/2022
#13. Write a program to calculate area of an equilateral triangle.
import math
a = int (input("Enter a value of sides of a triangle : "))
area = float((math.sqrt(3))*a*a/4)
print("The area of an equilateral triangle is = {}".format(area))