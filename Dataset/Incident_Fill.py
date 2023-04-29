# /usr/bin/env python3
import os
import csv
import pandas as pd

"""
This script was used to fill some of the offense codes missing in some of the datasets
"""
files = ["2015.csv", "2016.csv", "2017.csv", "2018.csv", "2019.csv", "2020.csv", "2021.csv", "2022.csv"]

Offense_Code_Group_file = "offense_codes_group.csv"
csvfile = open(Offense_Code_Group_file, newline="")
reader = csv.DictReader(csvfile)
Offense_Code_Group_Dict = {}
for row in reader:
    OFFENSE_CODE = row["OFFENSE_CODE"]
    OFFENSE_CODE_GROUP = row["OFFENSE_CODE_GROUP"]
    Offense_Code_Group_Dict[OFFENSE_CODE] = OFFENSE_CODE_GROUP

i = 0
for file in files:
    File_Data = []
    csvfile = open(file, newline="")
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = row['OFFENSE_CODE_GROUP']
        if (p == ''):
            Offense_Code = row["OFFENSE_CODE"]
            if Offense_Code not in Offense_Code_Group_Dict:
                Offense_Code = "0" + Offense_Code
            if Offense_Code not in Offense_Code_Group_Dict:
                continue
            Offense_Code_Group = Offense_Code_Group_Dict[Offense_Code]
            row['OFFENSE_CODE_GROUP'] = Offense_Code_Group
        else:
            print(row['OFFENSE_CODE_GROUP'])
        File_Data.append(row)
    df = pd.DataFrame(File_Data)
    df.to_csv("New_" + file, index=False)

