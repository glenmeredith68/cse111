import csv


def main():
    products_dict = read_dict('w09/products.csv', 0)
    print('ALL PRODUCTS')
    print()
    print(products_dict)
    print()
    with open('w09/request.csv', 'rt') as request_file:
        requests_dict = {}
        reader = csv.reader(request_file)
        print()
        print('REQUESTED ITEMS')
        print()
        for line in reader:
            product_id = line[0]
            if line[0] in products_dict:
                product_list = products_dict[product_id]
                product_name = product_list[1]
                quantity = line[1]
                price = int(quantity) * float(product_list[2])
                print(f'{product_name} * {quantity} = ${price:.2f}')


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


if __name__ == '__main__':
    main()