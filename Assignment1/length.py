#Author - Soumitra Das                                       Date - 15/12/2022
#5. Write a program to enter length in centimeter and convert it into meter and kilometer.
length=int(input("Enter length in centimeter: "))
meter=length/100
kilometer=length/100000
print("Length in meter is {} and kilometer is {}".format(meter,kilometer))