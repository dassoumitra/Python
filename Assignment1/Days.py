#Author - Soumitra Das                                    Date - 15/12/2022
#8. Write a program to convert days into years, weeks and days.
d = int (input("Enter a Days : "))
y = int(d/365)
r = d%365
w = int(r/7)
d1 = int(r%7)
print("{} days are equivalent to {} years , {} weeks and {} days".format(d,y,w,d1))