#Author - Soumitra Das                            Date - 24/01/2023
#4. WAP to input basic salary of an employee and calculate its Gross salary (Basic Salary + HRA + DA) according to following:
# Basic Salary less than or equal  10000 : HRA = 20%, DA = 80%
# Basic Salary less than or equal 20000 : HRA = 25%, DA = 90%
# Basic Salary greater than 20000 : HRA = 30%, DA = 95%

sa=int(input("Enter your salary : "))
if sa<=10000:
    hra=sa*(20/100)
    da=sa*(80/100)
    Gsa=sa+hra+da
    print("The Gross salary is {}".format(Gsa))
elif sa<=20000:
    hra=sa*(25/100)
    da=sa*(90/100)
    Gsa=sa+hra+da
    print("The Gross salary is {}".format(Gsa))
else:
    hra=sa*(30/100)
    da=sa*(95/100)
    Gsa=sa+hra+da
    print("The Gross salary is {}".format(Gsa))   
