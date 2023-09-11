#Author - Soumitra Das                               Date - 15/12/2022
#7. Write a program to enter temperature in Fahrenheit and convert to Celsius.
temf = float(input("Enter temperature in Fahrenheit : "))
c = (5*temf - 160)/9
print("{} is a Fahrenheit temperature and its equivalent Celsius temperature is = {}".format(temf,c))