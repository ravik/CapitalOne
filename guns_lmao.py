import csv
import sys
ret_array = []
with open("msa_dataset.csv", 'r', encoding='mac_roman', newline='') as csvfile:
    files = csv.DictReader(csvfile)
    for row in files:
        ret_array.append(row)
a = ret_array[0]

answer = []
for obj in ret_array:
    desc = (
        "<b>" + obj["Date"] + " " + obj["Title"] + "</b></br>Location: " +
        obj["Location"] + "</br>Deaths: " +
        obj["Number of Victim Fatalities"] +
        "&nbsp Injuries: " + obj["Number of Victims Injured"] +
        "</br>Shooter: " +
        obj["Average Shooter Age"] + "yo " +
        obj["Shooter Sex"] +
        "</br>" + obj["Description"]
    )
    par = {
        "type": "Feature",
        "properties": {
            "description": desc
        },
        "geometry": {
            "type": "point",
            "coordinates": [obj["Longitude"], obj["Latitude"]]
        }
    }
    answer.append(par)
import json
print(json.dumps(answer, indent=4))
