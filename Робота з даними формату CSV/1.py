import csv

import os

flag = False

try:

    csvfile = open("Ukraine_inflation.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ";")

    print("Year: Inflation, consumer prices (annual %)")

    for row in reader:

        print(row['Year'], ': ', row["Inflation, consumer prices (annual %)"])

    csvfile.close

except:

    print("Файл Ukraine_inflation.csv не знайдено!")

try:

    csvfile = open("Ukraine_inflation.csv","r")

    reader = csv.DictReader(csvfile, delimiter = ";")

    highest_inflation = float("-inf")
    lowest_inflation = float("inf")

    for row in reader:

        if float(row["Inflation, consumer prices (annual %)"]) > highest_inflation:

            highest_inflation = float(row["Inflation, consumer prices (annual %)"])

        if float(row["Inflation, consumer prices (annual %)"]) < lowest_inflation:

            lowest_inflation = float(row["Inflation, consumer prices (annual %)"])


    print("Year: Inflation, consumer prices (annual %)")

    print("Найвища інфляція:", highest_inflation)
    print("Найнижча інфляція:", lowest_inflation)

    with open("new_ukraine_inflation.csv","a") as csvfile2:

        writer = csv.writer(csvfile2, delimiter = ";")

        #writer.writerow((highest_inflation, lowest_inflation))
        
        writer.writerow(['Найнижча інфляція', str(lowest_inflation)])
        writer.writerow(['Найвища інфляція', str(highest_inflation)])

    csvfile.close

except:

    print("Файл Ukraine_inflation.csv не знайдено!")