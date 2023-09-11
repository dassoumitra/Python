#Author - Soumitra Das                                       Date - 15/12/2022
#4. Write a program to enter radius of a circle and find its diameter, circumference and area.
r=int(input("Enter a radius of a circle: "))
d=2*r
area=3.14*r*r
peri=d*3.14
print("The area of circle is = {}\nThe perimeter of a circle is= {}".format(area,peri))
