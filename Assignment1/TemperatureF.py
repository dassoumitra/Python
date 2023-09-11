#Author - Soumitra Das                                         Date - 15/12/2022
#6. Write a program to enter temperature in Celsius and convert it into Fahrenheit.
temc = float(input("Enter temperature in Celsius : "))
F = (9*temc+160)/5
print("{} is a Celsius temperature and its equivalent Fahrenheit temperature is = {}".format(temc,F))