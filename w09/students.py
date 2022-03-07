import csv


def main():
    student_dict = read_dict('students.csv')
    # i_number = input('What is the I-number you want to search? ')
    # name = input('What is yur name? ')

    # student_dict[i_number] = name
    # print(student_dict)
    if i_number in student_dict:
        print(student_dict[i_number])
        pass
    else:
        print('invalid I-number')


Student_dict = {
    '751766201': ['James Smith'],
    '751762102': ['Esther Einboden'],
    '052058203': ['Cassidy Benavidez'],
    '323021604': ['Joel Hatch'],
    '251041405': ['Brianna Ririe'],
    '001152306': ['Stefano Hisler'],
    '182706207': ['Hyeonbeom Park'],
    '124712708': ['Maren Thomas'],
    '212505409': ['Tyler Clark']
}


def read_dict(file_name):
    with open(file_name, 'rt') as students_file:
        reader = csv.reader(students_file)
        next(reader)
        students = {}
        for line in reader:
            number = line[0]
            full_name = line[1]
            students[number] = full_name

        return students


if __name__ == '__main__':
    main()
