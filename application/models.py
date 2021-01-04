from application import app, db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, DecimalField, SubmitField, SelectField

class Game_rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    rating_id = db.Column(db.Integer, db.ForeignKey('rating.id'))

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    platform = db.Column(db.Integer, nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    game_rating = db.relationship('Game_rating', backref='game')
    
class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(300), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    game_rating = db.relationship('Game_rating', backref='rating')