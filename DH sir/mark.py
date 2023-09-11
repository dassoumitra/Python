s1=int(input("Enter a marks for subject1 : "))
s2=int(input("Enter a marks for subject2 : "))
s3=int(input("Enter a marks for subject3 : "))
s4=int(input("Enter a marks for subject4 : "))
s5=int(input("Enter a marks for subject5 : "))
total=s1+s2+s3+s4+s5
ave=total//5
if(ave>=90):
    print("Grade is AA")
elif(ave>=80):
    print("Grade is A")
elif(ave>=75):
    print("Grade is B+")
elif(ave>=60):
    print("Grade is B")
elif(ave>=55):
    print("Grade is C")
elif(ave>=50):
    print("Grade is D")
else:
    print("Grade is F")

