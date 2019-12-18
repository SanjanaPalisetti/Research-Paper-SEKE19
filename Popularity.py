import csv
import os
import xlrd 
import xlwt 
from xlwt import Workbook 

views = 1

# s,c,a,f,v parameters are read from three files and the popularity is written into three new different files as well

with open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/EO-Body.csv', 'r') as inp1, open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/EA-Body.csv', 'r') as inp2,open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/AO-Body.csv', 'r') as inp3,open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/PopularityEO.csv', 'w') as out1,open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/PopularityEA.csv', 'w') as out2,open('/Users/sanjanapalisetti/Desktop/Desk/ESE/L1dataset/PopularityAO.csv', 'w') as out3:

    p = [None]*2000
    i=-1

    writer1 = csv.writer(out1)
    writer2 = csv.writer(out2)
    writer3 = csv.writer(out3)
    header = 'Post Link','Popularity'
    writer1.writerow(header)
    writer2.writerow(header)
    writer3.writerow(header)

    # For EO-Body.csv

    for row in csv.reader(inp1):

        i=i+1
        if i==0:
            continue
        s = float(row[13])  # row 13 contains all scores
        c = float(row[12])  # row 12 contains all comment counts
        a = float(row[11])  # row 11 contains all answer counts
        if row[15] == "" :  # row 15 contains all fav counts
            f = 0
        else :
            f = float(row[15])
        v = float(row[14])/views    # row 14 contains all view counts
        p[i-1] = s+a+c+f+v
        print(i-1," ",p[i-1])

        rowout = row[0],str(p[i-1])
        writer1.writerow(rowout)

    i=-1

    # For EA-Body.csv

    for row in csv.reader(inp2):

        i=i+1
        if i==0:
            continue
        s = float(row[13])
        c = float(row[12])
        a = float(row[11])
        if row[15] == "" :
            f = 0
        else :
            f = float(row[15])
        v = float(row[14])/views
        p[i-1] = s+a+c+f+v
        print(i-1," ",p[i-1])

        rowout = row[0],str(p[i-1])
        writer2.writerow(rowout)

    i=-1

    # For AO-Body.csv

    for row in csv.reader(inp3):

        i=i+1
        if i==0:
            continue
        s = float(row[13])
        c = float(row[12])
        a = float(row[11])
        if row[15] == "" :
            f = 0
        else :
            f = float(row[15])
        v = float(row[14])/views
        p[i-1] = s+a+c+f+v
        print(i-1," ",p[i-1])

        rowout = row[0],str(p[i-1])
        writer3.writerow(rowout)
