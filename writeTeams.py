import csv
from string import Template

with open('teams.csv', 'w', newline='') as f1, open('country_codes.csv', newline='') as f2:
    writer = csv.writer(f1)
    reader = csv.reader(f2)

    for row in reader:
        countryName = row[0]
        countryCode = row[1]
        teamURLTemplate = Template(
            'https://en.wikipedia.org/wiki/${country}_national_football_team').substitute(country=countryName.replace(' ', '_'))
        writer.writerow([row[1], row[0].upper(), teamURLTemplate])
