# The Body Mass Index (BMI) is one of the calculations used by doctors to assess an adult’s health. The doctor measures the patient’s height (in metres) and weight (in kilograms), then calculates the BMI using the formula
#
# BMI = weight/(height × height).
#
# Write a program which prompts for the patient’s height and weight, calculates the BMI, and displays the corresponding message from the table below.
#
# BMI Category	Message
# More than 25	Overweight
# Between 18.5 and 25.0 (inclusive)	Normal weight
# Less than 18.5	Underweight

w = float(input())
h = float(input())
bmi = w / (h * h)
if bmi > 25.0:
    print("Overweight")
elif 25.0 >= bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")
