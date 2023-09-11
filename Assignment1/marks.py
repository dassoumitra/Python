#Author - Soumitra Das                                  Date - 15/12/2022
#14. Write a program to enter marks of five subjects and calculate total, average and percentage.
sub1 = int(input("Enter marks of CP = "))
sub2 = int (input("Enter a marks of DS = "))
sub3 = int (input("Enter a marks of Python = "))
sub4 = int (input("Enter a marks of Algo = "))
sub5 = int (input("Enter a marks of CSO =  "))
total = sub1+sub2+sub3+sub4+sub5
ave = float(total/5)
per = float(total/500*100)
print("Total marks is = {} \n Average marks is = {} \n The Percentage is = {}".format(total,ave,per))