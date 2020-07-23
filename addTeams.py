import app
import csv

# adds teams to database
with open('teams.csv', newline='') as f:

    db = app.db

    reader = csv.reader(f)
    for row in reader:
        id = row[0]
        name = row[1]
        team_wiki_url = row[2]

        new_team = app.Team(id, name, team_wiki_url)

        db.session.add(new_team)
        db.session.commit()
