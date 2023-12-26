
# maths functions and number formatting 
print("Welcome to the tip calculator!")
# input bill from user
bill = int(input("What was the total bill? $"))
# input tip from user
tip = int(input("How much percentage tip would you like to give? 10, 12, or 15?"))
# input share from user
people = int(input("How many people to split the bill?"))
# convert calculated vale to match standard bill format
payment = "{:.2f}".format(round((bill+((tip/100)*bill))/people,2))
# print output
print(f"Each person should pay: {payment}")