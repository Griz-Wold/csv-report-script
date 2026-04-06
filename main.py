from argparse import ArgumentParser
from csv import DictReader
from statistics import median
from tabulate import tabulate

def get_cli_args():
    parser = ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True)
    parser.add_argument('--report', required=True)
    args = parser.parse_args()
    return args.files, args.report

def get_all_rows(files):
    all_rows = []
    try:
        for file in files:
            with open(file, 'r', encoding='utf-8') as csvfile:
                reader = DictReader(csvfile)
                for row in reader:
                    all_rows.append({'student': row['student'],
                                     'date': row['date'],
                                     'coffee_spent': int(row['coffee_spent']),
                                     'sleep_hours': float(row['sleep_hours']),
                                     'study_hours': float(row['study_hours']),
                                     'mood': row['mood'],
                                     'exam': row['exam']})
        return all_rows
    except FileNotFoundError:
        print('Файл не найден.')
        exit(1)

def get_median_coffee(rows):
    students = {}
    for row in rows:
        student = row['student']
        coffee = row['coffee_spent']
        if student not in students:
            students[student] = []
        students[student].append(coffee)

    median_coffee = []
    for student in students:
        median_coffee.append((student, median(students[student])))
    median_coffee = sorted(median_coffee, key=lambda item: item[1], reverse=True)
    return median_coffee

def main():
    files, report = get_cli_args()
    my_rows = get_all_rows(files)
    if report == 'median-coffee':
        print(tabulate(get_median_coffee(my_rows), headers=['student', 'median_coffee'], tablefmt='grid'))
    else:
        print('Неизвестный тип отчета.')
        exit(1)

if __name__ == '__main__':
    main()