from application import app, db
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, DecimalField, SubmitField, SelectField


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    rating = db.relationship('Rating', backref='game')
    
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'), nullable=False)

class GameForm(FlaskForm):
    user_name = StringField('Enter your Username')
    game_name = StringField('Name of Game')
    game_review = StringField('Review of Game')
    game_rating = SelectField(u'Select a Rating Out of 5', choices=[('1','One'), ('2','Two'),('3','Three'),('4','Four'),('5','Five')])
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    game_name = StringField('Enter Name of Game: ')
    platform_name = IntegerField('Enter No. Platform: ')
    genre_name = StringField('Enter Genre: ')
    submit = SubmitField('Submit')
    