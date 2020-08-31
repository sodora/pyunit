import csv


def drive_data(csv_file):
    data = {}
    with open(csv_file, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    for row in result:
        if len(row) > 1 and row[0].find('#') != 0:
            data[row[0]] = row[1:]
    return data
