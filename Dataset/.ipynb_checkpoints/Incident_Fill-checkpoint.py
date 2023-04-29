# /usr/bin/env python3
import os
import csv

"""
This script was used to fill some of the offense codes missing in some of the datasets
"""
files = ["2015.csv", 2016.csv, 2017.csv, 2018.csv, 2]

files = os.listdir()
for file in files:
    if not file.endswith("csv"):
        continue

    csvfile = open(file, newline="")
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
