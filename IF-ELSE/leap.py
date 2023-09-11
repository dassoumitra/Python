#Author - Soumitra Das                            Date - 24/01/2023
#3. WAP to check whether a year is leap year or not. 
y=int(input("Enter a year : "))
if((y%4==0 and y%100!=0) or y%400==0):
    print("The given year is a leap year.")
else:
    print("The given year is not a leap year.")
    