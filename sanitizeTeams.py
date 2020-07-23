import requests
import csv
from bs4 import BeautifulSoup

# go through csv of teams and check which links are valid
with open('teams.csv', newline='') as f:

    reader = csv.reader(f)
    for row in reader:
        countryCode = row[0]
        countryName = row[1]
        teamURL = row[2]

        wikiData = requests.get(teamURL)
        wikiSoup = BeautifulSoup(wikiData.text, 'html.parser')
        # heading will say '____' national football team if link is valid
        heading = wikiSoup.find(id='History')
        if (heading == None):
            print(countryCode + ' ' + countryName + ' ' + teamURL)
        else:
            print('History' + countryName)
