# National-Team-Mapper
User can select a country with a national or official football team, and then they can view a map of where the players on that team were born.

# To Do
- [x] Complete About section
- [x] Add images and make About section aesthetically pleasing
* Make sure selected countries show up on map (in light blue) - ADD French-Guiana's players - ADD Tahiti's players (French Polynesia) - ADD Nigeria's players - ADD Peru - ADD Samoa - ADD Sri Lanka
* Add in info about date the data was scraped - FIX margin around this
- [x] Make the site mobile-responsive
* Clean up files and file structure
* Find out how to set up analytics (or just how to check them)
* Deploy the app to a hosting service (Likely linode)

```python
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
```

# Sources
France squad photo: https://www.quora.com/What-would-France-national-football-team-do-without-African-origin-players
BeautifulSoup logo: https://funthon.wordpress.com/2017/05/21/beautiful-soup-4/
Algeria flag: https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/900px-Flag_of_Algeria.svg.png