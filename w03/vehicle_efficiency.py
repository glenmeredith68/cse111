#The goal of this program is to print mpg and liters per 100km using three functions

def main():
    # Get an odometer value in U.S. miles from the user.
    odometer_start = int(input('What is the starting odometer? '))
    # Get another odometer value in U.S. miles from the user.
    odometer_end = int(input('What is the ending odometer? '))
    # Get a fuel amount in U.S. gallons from the user.
    gallons_used = float(input('How many gallons of gas did you use? '))
    # Call the miles_per_gallon function and store
    # the result in a variable named mpg.
    mpg = miles_per_gallon(odometer_start, odometer_end, gallons_used)
    # Call the lp100k_from_mpg function to convert the
    # miles per gallon to liters per 100 kilometers and
    # store the result in a variable named lp100k.
    lp100k = lp100k_from_mpg(mpg)
    # Display the results for the user to see.
    print(f'Your car gets {mpg:.2f} mpg and {lp100k:.2f} lp100k. ')
    pass


def miles_per_gallon(start_miles, end_miles, amount_gallons):
    """Compute and return the average number of miles
    that a vehicle traveled per gallon of fuel.

    Parameters
        start_miles: An odometer value in miles.
        end_miles: Another odometer value in miles.
        amount_gallons: A fuel amount in U.S. gallons.
    Return: Fuel efficiency in miles per gallon.
    """
    denominator = end_miles - start_miles
    numerator = amount_gallons
    mpg = denominator / numerator
    return mpg


def lp100k_from_mpg(mpg):
    """Convert miles per gallon to liters per 100
    kilometers and return the converted value.

    Parameter mpg: A value in miles per gallon
    Return: The converted value in liters per 100km.
    """
    lp100k = 235.215 / mpg
    return lp100k


# Call the main function so that
# this program will start executing.
main()