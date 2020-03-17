import math
Weight=float(input("What is your Weight in Kilograms?"))
#Asking user to input their weight in Kilograms, storing weight as a float variable
Height = float (input("What is your height Centimeters"))
#Asking user to input their height in Centimeters, storing height as a float variable
BMI = round((Weight/Height**2)*10000)
#Creating a variable called BMI, using BMI calc taking given Height & Weight and formula(W/H**2)and multiplying it by 100000

print("Your BMI = ",BMI)
# printing out calculated BMI
