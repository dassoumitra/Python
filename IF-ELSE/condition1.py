#Author - Soumitra Das                            Date - 24/01/2023
#1. 60% of attendance is required to appear in the final semester. Input number of classes conducted by a teacher and number of classes attended by a student. Based on the input information, print if that student is eligible to appear in the final semester or not. 

att=int(input("Enter a percentage of attendence : "))
if att>=60:
    print("Student is eligible to appear in the final semester.")
else:
    print("Student is not eligible to appear in the final semester.")