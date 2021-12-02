print("Welcome ot the tip calculator!")

#Get inputs by the user
bill = float(input("What is the total bill? $ "))
tip = int(input("How much would you like to give? 10, 12 or 15? "))
people = int(input("How many people to splitt the bill? "))

#calculate the bill
total_bill = bill + bill * tip / 100

#Calculate per people
calculation = total_bill / people

#Round and print
calculated = round(calculation,2)
calculated = "{:.2f}".format(calculation)
print(f"Each person should pay: ${calculation}" )from flask import Flask
