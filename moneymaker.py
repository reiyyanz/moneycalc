import math as math
import random as rd

#wisconsin tax
state = input("What state do you live in?:")
fedtax = .0543
statetax = .0765

wage = int(input("What is your hourly wage?:"))
hours = int(input("How many hours did you work this pay period?:"))

b4tax = wage * hours
print(f"Your pay before taxes is: ${b4tax}")

afterfedtax = (b4tax * fedtax)
afterstatetax = (b4tax * statetax)
aftertax = b4tax - afterfedtax - afterstatetax

print(f"In {state}, after taxes your pay is: ${aftertax}")







