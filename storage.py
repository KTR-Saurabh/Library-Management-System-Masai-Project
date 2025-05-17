# storage.py
import csv
import os
from utils import get_data_file

def read_csv(filename):
    file_path = get_data_file(filename)
    if not os.path.exists(file_path):
        return []
    with open(file_path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def write_csv(filename, data, fieldnames):
    file_path = get_data_file(filename)
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def append_csv(filename, row, fieldnames):
    file_path = get_data_file(filename)
    exists = os.path.exists(file_path)
    with open(file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not exists:
            writer.writeheader()
        writer.writerow(row)