# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    # Call the compute_age, kg_from_lb, cm_from_in,
    # body_mass_index, and basal_metabolic_rate functions
    # as needed.
    gender = input("Please enter your gender (M or F): ")
    birthdate = input("Enter your birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter your weight in U.S. pounds: "))
    height = float(input("Enter your height in U.S. pounds: "))

    Age = compute_age(birthdate)
    Kilos = float(kg_from_lb(weight))
    Cms = float(cm_from_in(height))
    bmi = float(body_mass_index(Kilos, Cms))
    bmr = float(basal_metabolic_rate(gender, Kilos, Cms, Age))

    # Print the results for the user to see.
    print(f"Age (years): {Age}")
    print(f"Weight (kg): {Kilos}")
    print(f"Height (cm): {Cms}")
    print(f"Body mass index: {bmi}")
    print(f"Basal metabolic rate (kcal/day): {bmr}")

    pass


def compute_age(birth_str):
    """Compute and return a person's age in years.
    Parameter birth_str: a person's birthdate stored
        as a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    # Convert a person's birthdate from a string
    # to a date object.
    birthdate = datetime.strptime(birth_str, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the
    # person's birthdate in years.
    years = today.year - birthdate.year

    # If necessary, subtract one from the difference.
    if birthdate.month > today.month or \
        (birthdate.month == today.month and \
            birthdate.day > today.day):
        years -= 1

    return years


def kg_from_lb(weight):
    """Convert a mass in pounds to kilograms.
    Parameter pounds: a mass in U.S. pounds.
    Return: the mass in kilograms.
    """
    weight_in_kg = weight * 0.453592


    return weight_in_kg


def cm_from_in(height):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """
    height_in_cm = height * 2.54
    
    return height_in_cm


def body_mass_index(weight_in_kg, height_in_cm):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi = round(weight_in_kg * 10000 / height_in_cm**2)

    return bmi


def basal_metabolic_rate(gender, weight_in_kg, height_in_cm, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender == "M":
        bmr = round(88.362 + 13.397*weight_in_kg + 4.799*height_in_cm - 5.677*age)
    elif gender == "F":
        bmr = round(447.593 + 9.247*weight_in_kg + 3.098*height_in_cm - 4.330* age)
    return bmr


# Call the main function so that
# this program will start executing.
main ()