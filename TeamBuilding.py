from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(100), nullable=False)
    members = db.relationship('Member', backref='team', lazy=True)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=True)

@app.route('/create_team', methods=['POST'])
def create_team():
    team_name = request.form.get('team_name')
    new_team = Team(team_name=team_name)
    db.session.add(new_team)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/join_team/<int:team_id>', methods=['GET'])
def join_team(team_id):
    member_name = request.args.get('member_name')
    member = Member(name=member_name, team_id=team_id)
    db.session.add(member)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/')
def home():
    teams = Team.query.all()
    return render_template('home.html', teams=teams)

if _name_ == '_main_':
    db.create_all()
    app.run(debug=True)