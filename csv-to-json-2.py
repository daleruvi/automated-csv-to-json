import csv
import json
import os

with open(r"data/data.csv", newline="") as csvfile:
    print(csvfile.read().split("\n")[0])
    reader = csv.DictReader(csvfile, delimiter=',')
    data = [row for row in reader]

with open(r"data/output.json", "w") as jsonfile:
    json.dump(data, jsonfile)
