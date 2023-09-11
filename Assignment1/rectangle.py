#Author - Soumitra Das                                     Date - 15/12/2022
#3. Write a program to enter length and breadth of a rectangle and find its area.
len=int(input("Enter a value of a length of a rectangle : "))
bread=int(input("Enter a value of a breadth of a rectangle : "))
area=int(len*bread)
peri=2*(len+bread)
print("Area = {}\nPerimeter = {}".format(area,peri))