#If the bill was $150.00, split between 5 people, with 12% tip. 

print("Welcome to the tip calculator")

total=float(input("What was the total bill? $"))

percentage_tip=float(input("What percentage tip would you like to give? 10, 12, or 15? "))

no_of_person=int(input("How many people to split the bill? "))

tip=float(total*(percentage_tip/100))

total+=tip

split="{:.2f}".format(total/no_of_person)

print(f"Each person should pay: ${split}")

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
