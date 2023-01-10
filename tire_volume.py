import math
from datetime import date

current_date_and_time = (date.today()).strftime("%Y-%m-%d")


w = float(input("Enter the width of the tire in mm (ex 205): "))
a = float(input("Enter the aspect ratio of the tire (ex 60): "))
d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

v = float((math.pi * w**2 * a*(w * a + 2540 * d))/10000000000)

print(f"The approximate volume is {v: .2f} liters")

with open("volumes.txt", "at") as volumes_file:
    print(f"Date: {current_date_and_time}, width: {w: .2f}, aspect ratio: {a: .2f}, diameter: {d: .2f}, volume: {v: .2f}", file=volumes_file)

print("Thank you, your date and data promped were successfully added to our registry")    

more_data = input("Would you like to add more data? (Yes/No): ")

if more_data == "Yes":

    current_date_and_time = (date.today()).strftime("%Y-%m-%d")

    w = float(input("Enter the width of the tire in mm (ex 205): "))
    a = float(input("Enter the aspect ratio of the tire (ex 60): "))
    d = float(input("Enter the diameter of the wheel in inches (ex 15): "))

    v = float((math.pi * w**2 * a*(w * a + 2540 * d))/10000000000)

    print(f"The approximate volume is {v: .2f} liters")

    with open("volumes.txt", "at") as volumes_file:
        print(f"Date: {current_date_and_time}, width: {w: .2f}, aspect ratio: {a: .2f}, diameter: {d: .2f}, volume: {v: .2f}", file=volumes_file)

    print("Thank you, your date and data promped were successfully added to our registry")    

elif more_data == "No":
    print("Good bye!")

else: 
    print("Error!")