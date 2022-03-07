from datetime import datetime 



def main():
    
    print("Welcome to the BMI & BMR Conversion Machine.")

    gender = input("What is your gender: (M/F) ")

    birth_str = input("What is your DoB: (YYYY-MM-DD) ")

    weight = float(input("What is your weight in pounds:( US lbs ). "))

    height = float(input("What is your height in inches:( only inches ) "))
    
    age = compute_age(birth_str)
    
    kg_weight = kg_from_lb(weight)

    cm_height = cm_from_in(height)

    bmi_index = body_mass_index(kg_weight,cm_height)

    bmr_index = basal_metabolic_rate(gender, kg_weight, cm_height, age)

    print(f"Age (years): {age}")
    print(f"Weight (kg): {kg_weight:.2f}")
    print(f"Height (cm): {cm_height:.1f}")
    print(f"Body mass index: {bmi_index:.1f}")
    print(f"Basal metabolic rate (kcal/day): {bmr_index:.0f}")

    
    
    

    

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
    kg = weight * .45359237
    
    return kg


def cm_from_in(inches):
    """Convert a length in inches to centimeters.
    Parameter inches: a length in inches.
    Return: the length in centimeters.
    """ 
    cm = inches * 2.54
    float(f'{cm:.2f}')
    return cm


def body_mass_index(weight, height):
    """Compute and return a person's body mass index.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
    Return: a person's body mass index.
    """
    bmi =  weight / (height ** 2) * 10000
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Compute and return a person's basal metabolic rate.
    Parameters
        weight: a person's weight in kilograms.
        height: a person's height in centimeters.
        age: a person's age in years.
    Return: a person's basal metabolic rate in kcals per day.
    """
    if gender.upper() == 'M':
        bmr = 88.362 + 13.397 * weight + 4.799 * height - 5.677 * age 
        return bmr
    else:
        bmr = 447.593 + 9.247 * weight + 3.098 * height - 4.330 * age
        
        return bmr

main()

# Call the main function so that
# this program will start executing.


