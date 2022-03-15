import csv
from datetime import datetime


def main():
    products_dict = read_dict('w10/products.csv', 0)
    print('ALL PRODUCTS')
    print()
    print(products_dict)
    print()


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
    with open(filename, 'rt') as products_file:
        reader = csv.reader(products_file)
        next(reader)
        products_dict = {}
        for line in reader:
            products_dict[line[key_column_index]] = [line[0], line[1], line[2]]
        return products_dict


def print_receipt():
    print('Broulim\'s')
    products_dict = read_dict('w10/products.csv', 0)
    with open('w10/request.csv', 'rt') as request_file:
        requests_dict = {}
        reader = csv.reader(request_file)
        print()
        print('REQUESTED ITEMS')
        print()
        total_items = 0
        subtotal = 0
        for line in reader:
            product_id = line[0]
            if line[0] in products_dict:
                product_list = products_dict[product_id]
                product_name = product_list[1]
                quantity = line[1]
                total_items += 1
                price = int(quantity) * float(product_list[2])
                subtotal += price
                print(f'{product_name} * {quantity} = ${price:.2f}')
        sales_tax = 1.06
        total = subtotal * 1.06
        curr_date_time = datetime.now()
        print(f'You bought {total_items} items today. ')
        print(f'Subtotal: {subtotal}')
        print(f'Total (after 6% tax): {total}')
        print('Thanks for shopping with us today! Come back soon :) ')
        print(f'- - --{curr_date_time:%A %I %M %p}-- - -')


if __name__ == '__main__':
    main()