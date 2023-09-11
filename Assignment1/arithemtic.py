#Author - Soumitra Das                                     Date - 15/12/2022
#2. Write a program to enter two numbers and perform all arithmetic operations.
num1=int(input("Enter a value of num1: "))
num2=int(input("Enter a value of num2: "))
#operator=int(input("Enter an operator symbol("+,-,*,/,%"): "))
add=num1+num2
sub=num1-num2
mul=num1*num2
dibi=float(num1/num2)
mod=num1%num2
print("The addition of {} and {} is = {}\nThe substraction of {} and {} is = {}\nThe multiplication of {} and {} is = {}\nThe divition of {} and {} is ={}\nThe Remainder Of {} and {} ={}".format(num1,num2,add,num1,num2,sub,num1,num2,mul,num1,num2,dibi,num1,num2,mod))