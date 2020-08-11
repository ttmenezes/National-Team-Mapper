# National-Team-Mapper
User can select a country with a national or official football team, and then they can view a map of where the players on that team were born.

This project was inspired by a research presentation about France's national football team. The presentation outlined how players with heritage from
current and former colonies and territories are ubiquitous in France's squad and largely responsible for the recent successes of the team.

I wanted to dig deeper into this topic and see how other imperial states have leveraged current and former colonies to strengthen their national teams today. Hence, I built a program which uses Beautiful Soup to scrape the roster data for each national team and records the birthplaces of its players (if available on Wikipedia). I then built a full-stack web application using Flask which displays a vector map showing a visual representation of the potentially fragmented origins of players on a given national team.

## Quick Start
Run `writeTeams.py` which uses the country-code data from `country_codes.csv` to write to `teams.csv` to record a country's ISO-code, its name, and the Wikipedia site for its national football team.
```
python3 writeTeams.py
```
Run `sanitizeTeams.py` to check which teams do not have a Wikipedia page that follows the typical URL format (https://en.wikipedia.org/wiki/${country}_national_football_team) after running this, go through and update or remove the URLs which do not lead to the correct Wikipedia page for a given national team.
```
python3 sanitizeTeams.py
```
Run `getSquad.py` which goes through every national team in `teams.csv` and scrapes the birthplaces for each player on a given team from their individual Wikipedia page. This data is then written to `players.csv`.
```
python3 getSquad.py
```
Run `addTeams.py` and `addPlayers.py` to add the team and player data to the app's sqlite database `db.sqlite`.
```
python3 addTeams.py
python3 addPlayers.py
```
Either run a development server via `app.py` or deploy this Flask app to production.
```
python3 app.py
```

### Production deployment is visible at http://nationalteam.tech

## Frameworks and Libraries Used
* Beautiful Soup (python)
* Flask (python)
* jVectorMap (javascript)
* jQuery (javascript)
* Nginx (web server)
* Gunicorn (web server)

## Sources
* Javascript vector map library: https://jvectormap.com/
* France squad photo: https://www.quora.com/What-would-France-national-football-team-do-without-African-origin-players
* Beautiful Soup logo: https://funthon.wordpress.com/2017/05/21/beautiful-soup-4/
* Algeria flag: https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Flag_of_Algeria.svg/900px-Flag_of_Algeria.svg.png