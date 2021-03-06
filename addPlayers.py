import app
import csv

# adds players to database
with open('players.csv', newline='') as f:

    db = app.db

    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        player_wiki_url = 'https://en.wikipedia.org' + row[1]
        team_id = row[2]
        birthplace = row[3]
        birth_country = row[4]

        # input for Player: (name, player_wiki_url, team_id, birthplace, birth_country)
        new_player = app.Player(
            name, player_wiki_url, team_id, birthplace, birth_country)

        db.session.add(new_player)
        db.session.commit()
