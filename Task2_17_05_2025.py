# Write a script to calculate the area and perimeter of a rectangle using variables. 
length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)
print("Area of the rectangle:", area)
print("Perimeter of the rectangle:", perimeter)


# Write a script that takes two numbers as input and prints  whether the first number is greater than, less than, or equal to the second number.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print("The first number is greater than the second.")
elif num1 < num2:
    print("The first number is less than the second.")
else:
    print("Both numbers are equal.")

# Write a script that checks if a given year is a leap year (divisible by 4, but not by 100 unless also divisible by 400). 

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
#Experiment with different arithmetic and logical operators in the interpreter. 

>>>4+5
9
>>>9*3
27
>>>2**2
4
>>>10/5
2
>>> not(4>3)
False
>>> (5>8 and 6<7)
False
>>> 7>5 or 6>7
True
>>>exit()

# Write a script that concatenates two strings and prints the result.
str1="Jyothi"
str2 ="Karumuri"
print(str1+str2)
