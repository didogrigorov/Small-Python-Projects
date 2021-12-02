#Get user input
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

#Calculate BMI
bmi = round(weight / height ** 2)

#Return condition
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you are normal weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are overweight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese")
else:
  print("clinically obese")
