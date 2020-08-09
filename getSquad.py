import requests
import sys
import csv
from bs4 import BeautifulSoup
from string import Template

# make table of country codes
with open('teams.csv', newline='') as f:
    reader = csv.reader(f)
    countryCodes = {}
    for row in reader:
        countryCodes[row[1]] = row[0]
    f.close()


def getBirthplace(wikiURL):
    # given url to the player's wiki, return their birthplace
    try:
        playerURLTemplate = Template(
            'https://en.wikipedia.org${url}').substitute(url=wikiURL)
        playerWikiData = requests.get(playerURLTemplate)
        playerWikiSoup = BeautifulSoup(playerWikiData.text, 'html.parser')
        return playerWikiSoup.find("td", class_="birthplace").get_text().strip()
    except:
        return None


def addSquad(team_id, teamWikiURL, writer):
    wikiData = requests.get(teamWikiURL)
    wikiSoup = BeautifulSoup(wikiData.text, 'html.parser')

    # If you want to access just the current roster, then use this section of code
    # squadRoster = wikiSoup.find(id='Current_squad')
    # nextEls = squadRoster.next_elements
    # for el in nextEls:
    #     if el.name == 'table':
    #         roster = el
    #         break
    # playerList = roster.find_all("tr", class_="nat-fs-player")

    # otherwise, if you want to also include recent call-ups, then use this line
    playerList = wikiSoup.find_all("tr", class_="nat-fs-player")

    for playerRow in playerList:
        player = playerRow.find(attrs={"scope": "row"})
        try:
            # for each player, record their birthplace and team
            birthplace = getBirthplace(player.a['href']).translate(
                str.maketrans('', '', '!@#$[]1234567890'))

            birth_country_name = birthplace.split(', ').pop()

            if birth_country_name.upper() in countryCodes:
                birth_country_id = countryCodes[birth_country_name.upper()]
            else:
                birth_country_id = '##'

             # input for object: (self, id, name, player_wiki_url, team_id, birthplace, birth_country)
            writer.writerow([player.get_text(), player.a['href'], team_id,
                             birthplace, birth_country_id])

        except:
            pass


# open file, iterate over teams, call method to put each player into the file
with open('players.csv', 'w', newline='') as f1, open('teams.csv', newline='') as f2:
    writer = csv.writer(f1)
    reader = csv.reader(f2)

    for row in reader:
        team_id = row[0]
        print(team_id + ' : ' + row[1])
        teamWikiURL = row[2]
        addSquad(team_id, teamWikiURL, writer)

    f1.close()
    f2.close()
