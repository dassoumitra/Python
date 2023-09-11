#Author - Soumitra Das                            Date - 24/01/2023
#5. WAP to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
bill=int(input("Enter electic bill :"))
if bill<=50:
    bill=bill*.50
elif bill<=150:
    bill=50*.5+(bill-50)*.75
elif bill<=250:
    bill=50*.5+100*.75+(bill-150)*1.20
else:
    bill=50*.5+100*.75+100*1.20+(bill-250)*1.50
addi=bill*.2
tbill=bill+addi
print("Total electricity bill is {}".format(tbill))

