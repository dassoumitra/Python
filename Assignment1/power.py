#Author - Soumitra Das                               Date - 15/12/2022
#9. Write a program to find power of any number x ^ y.
import math
x = int (input("Enter a value of x : "))
y = int (input("Enter a value of y : "))
power = pow(x,y)
print("Power of {}^{} is {}".format(x,y,power))