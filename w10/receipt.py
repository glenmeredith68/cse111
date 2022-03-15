import csv
from datetime import datetime
import sys


def main():

    products_dict = read_dict('w10/products.csv', 0)
    # print('ALL PRODUCTS')
    # print()
    # print(products_dict)
    # print()
    print_receipt(products_dict)


def calc_tip():
    tip = float(input('How much do you want to tip? '))
    return tip


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    try:
        with open(filename, 'rt') as products_file:
            reader = csv.reader(products_file)
            next(reader)
            products_dict = {}
            for line in reader:
                products_dict[line[key_column_index]] = [
                    line[0], line[1], line[2]
                ]
            return products_dict
    except FileNotFoundError as file_not_found_err:
        print(f'Error: {file_not_found_err}')
        print(
            'Looks like we\'re missing one of the files for your shopping experience. Please try again or emain mer16014@byui.edu :)'
        )
        sys.exit(1)


def print_receipt(products_dict):
    try:
        print('Broulim\'s')
        with open('w10/request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print()
            print('REQUESTED ITEMS')
            print()
            total_items = 0
            subtotal = 0
            for line in reader:
                product_id = line[0]
                # if line[0] in products_dict:
                product_list = products_dict[product_id]
                product_name = product_list[1]
                quantity = line[1]
                total_items += int(quantity)
                price = int(quantity) * float(product_list[2])
                subtotal += price
                print(f'{product_name}: {quantity} @ ${product_list[2]}')
            sales_tax = subtotal * .06
            tip = calc_tip()
            total = subtotal + sales_tax + tip
            curr_date_time = datetime.now()
            print()
            print(f'You bought {total_items} items today. ')
            print(f'Subtotal: ${subtotal:.2f}')
            print(f'Sales tax: ${sales_tax:.2f}')
            print(f'Tip: {tip}')
            print(f'Total: ${total:.2f}')
            print('Thanks for shopping with us today! Come back soon :) ')
            print(f'-- {curr_date_time:%A %b %d %I:%M %p %Y} --')

    except FileNotFoundError as file_not_found_err:
        print(f'Error: {file_not_found_err}')
        print(
            'Looks like we\'re missing one of the files for your shopping experience. Please try again or emain mer16014@byui.edu :)'
        )

    except PermissionError as permission_err:
        print(f'Error: {permission_err}')
        print(
            'Looks like you don\'t have the right file permissions for your shopping experience. Please try again or email mer16014@byui.edu :)'
        )

    except KeyError as key_err:
        print(f'Error: {key_err}')
        print(
            'Looks like we have a key error. Please try again or email mer16014@byui.edu :)'
        )


if __name__ == '__main__':
    main()