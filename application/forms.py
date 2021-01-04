from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, DateField, DecimalField, SubmitField, SelectField
from wtforms.validators import DataRequired

class GameForm(FlaskForm):
    user_name = StringField('Enter your Username: ', validators=[DataRequired()])
    game_name = StringField('Name of Game: ', validators=[DataRequired()])
    game_review = StringField('Review of Game: ', validators=[DataRequired()])
    game_rating = SelectField(u'Select a Rating Out of 5', choices=[('1','One'), ('2','Two'),('3','Three'),('4','Four'),('5','Five')])
    submit = SubmitField('Submit')

class AddForm(FlaskForm):
    game_name = StringField('Enter Name of Game: ', validators=[DataRequired()])
    platform_name = IntegerField('Enter No. Platform: ', validators=[DataRequired()])
    genre_name = StringField('Enter Genre: ', validators=[DataRequired()])
    submit = SubmitField('Submit')