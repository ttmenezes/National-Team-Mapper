from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Team Class/Model
class Team(db.Model):
    id = db.Column(db.String(2), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    team_wiki_url = db.Column(db.String(200))

    players = db.relationship('Player', backref='team', lazy=True)

    def __init__(self, id, name, team_wiki_url):
        self.id = id
        self.name = name
        self.team_wiki_url = team_wiki_url

    def __repr__(self):
        return f"Team: '{self.id}' - '{self.name}', '{self.team_wiki_url}'"


# Player Class/Model
class Player(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50))
    player_wiki_url = db.Column(db.String(200))
    team_id = db.Column(db.String(2), db.ForeignKey('team.id'), nullable=False)
    birthplace = db.Column(db.String(50))
    birth_country = db.Column(db.String(2))

    def __init__(self, name, player_wiki_url, team_id, birthplace, birth_country):
        self.name = name
        self.player_wiki_url = player_wiki_url
        self.team_id = team_id
        self.birthplace = birthplace
        self.birth_country = birth_country

    def __repr__(self):
        return f"Player: '{self.id}' - '{self.name}', '{self.team_id}', '{self.player_wiki_url}', '{self.birthplace}', '{self.birth_country}'"


# Team schema
class TeamSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'team_wiki_url')


# Player schema
class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'player_wiki_url',
                  'birthplace', 'birth_country')


# Init schema
team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)


# Landing page
@app.route('/')
def home():
    all_teams = Team.query.all()
    result = teams_schema.dump(all_teams)
    return render_template('index.html', team_data=result)


# Team info
@app.route('/<teamID>')
def get_team(teamID):
    all_teams = Team.query.all()
    result = teams_schema.dump(all_teams)

    roster = db.session.query(Player).filter(Player.team_id == teamID).all()

    rosterList = []

    for player in roster:
        rosterList.append({
            'name': player.name.translate({
                ord('\n'): None,
                ord('"'): None
            }),
            'wiki': player.player_wiki_url,
            'birthplace': player.birthplace.translate({
                ord('\n'): None,
                ord('"'): None
            }),
            'birth_country': player.birth_country
        })

    print(rosterList)

    return render_template('index.html', team_data=result, roster_data=rosterList, team_id=teamID)


# Get All teams
@app.route('/teams', methods=['GET'])
def get_products():
    all_teams = Team.query.all()
    result = teams_schema.dump(all_teams)
    return jsonify(result)


# Get Team Roster of Players
@app.route('/team/<teamID>', methods=['GET'])
def get_product(teamID):
    roster = db.session.query(Player).filter(Player.team_id == teamID).all()
    return players_schema.jsonify(roster)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)

# Create a Product
# @app.route('/product', methods=['POST'])
# def add_product():
#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     new_product = Team(name, description, price, qty)

#     db.session.add(new_product)
#     db.session.commit()

#     return product_schema.jsonify(new_product)

# Update a product
# @app.route('/product/<id>', methods=['PUT'])
# def update_product(id):
#     product = Team.query.get(id)

#     name = request.json['name']
#     description = request.json['description']
#     price = request.json['price']
#     qty = request.json['qty']

#     product.name = name
#     product.description = description
#     product.price = price
#     product.qty = qty

#     db.session.commit()

#     return product_schema.jsonify(product)


# Delete = Product
# @app.route('/product/<id>', methods=['DELETE'])
# def delete_product(id):
#     product = Team.query.get(id)
#     db.session.delete(product)
#     db.session.commit()

#     return product_schema.jsonify(product)
