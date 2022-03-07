def main():
    provinces_list = make_list('w09/provinces.txt')
    provinces_list.pop()
    provinces_list.pop(0)

    albertas = 0
    for line in provinces_list:
        if line == 'AB':
            line = 'Alberta'
        if line == 'Alberta':
            albertas += 1

    print(f'There are {albertas} Albertas in the modified list. ')


def make_list(file_name):
    with open(file_name, 'rt') as provinces_file:
        provinces_list = []
        for line in provinces_file:
            clean_line = line.strip()
            provinces_list.append(clean_line)
        return provinces_list


if __name__ == '__main__':
    main()