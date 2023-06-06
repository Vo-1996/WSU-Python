import sys

name = str(input("What is your name?:"))
first_number = int(input("Please give me your first number:"))
second_number = int(input("Please give me your second number:"))
final_number = first_number * second_number
print("Hello, " + name)
print("The result of "  + str(first_number) + " x " + str(second_number) + " is " + str(final_number))