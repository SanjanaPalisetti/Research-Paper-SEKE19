import csv
with open('Location&GPS.csv', 'r') as inp, open('/Users/sanjanapalisetti/Desktop/Desk/ESE/Filtered.csv', 'w') as out:
    writer = csv.writer(out)
    writer.writerow(next(csv.reader(inp)))
    for row in csv.reader(inp):    
        if "accuracy" in row[4] or "accuracy" in row[5] or "Accuracy" in row[4] or "Accuracy" in row[5] or "ACCURACY" in row[4] or "ACCURACY" in row[5] or "ENERGY" in row[4] or "ENERGY" in row[5] or "energy" in row[4] or "energy" in row[5] or "Energy" in row[4] or "Energy" in row[5] or "battery" in row[4] or "battery" in row[5] or "Battery" in row[4] or "Battery" in row[5] or "BATTERY" in row[4] or "BATTERY" in row[5] or "power" in row[4] or "power" in row[5] or "Power" in row[4] or "Power" in row[5] or "POWER" in row[4] or "POWER" in row[5]:
            writer.writerow(row)
