from csv import DictReader
import pandas as pd

# read csv file as a list of lists
with open(r'Dataset\boston_weather_data.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = DictReader(read_obj)
    # Pass reader object to list() to get a list of lists
    weather = list(csv_reader)

with open(r'Dataset\New_Dataset.csv', 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = DictReader(read_obj)
    # Pass reader object to list() to get a list of lists
    incidents = list(csv_reader)

new_Incident_Data = []
i = -1
days_dict = {}

for day in weather:
    date = day["time"]
    days_dict[date] = day["tavg"]

for entry in incidents:
    i += 1
    day = entry["OCCURRED_ON_DATE"].split(" ")[0]
    try:
        temp = days_dict[day]
    except:
        continue
    entry["AVERAGE_TEMPERATURE"] = temp
    new_Incident_Data.append(entry)

df = pd.DataFrame(new_Incident_Data)
df.to_csv("New_Dataset_Temperature.csv", index=False)