from application import app, db
from application.models import Game, GameForm, Rating, AddForm
from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy.sql import func


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/rating')
def rating():
    return render_template('rating.html')

@app.route('/addrating', methods=['GET', 'POST'])
def addrating():
    error=""
    form = GameForm()
    if request.method == 'POST':
        user_name = form.user_name.data
        game_name = form.game_name.data
        game_review = form.game_review.data
        game_rating = form.game_rating.data
        game_details = Game.query.filter_by(name=game_name).first()
        #review_details = Rating.query.filter_by(name=game_name).filter_by(username=user_name).first()
        if len(game_name) == 0 or len(game_review) == 0:
            error = "Please give a name to the game you want to review"
        else:
            new_review = Rating(username = user_name, name = game_name, review = game_review, rating = game_rating, game_id = game_details.id)
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for("rating"))

    return render_template('ratingform.html', form = form, message = error)

@app.route('/searchrating', methods=['GET','POST'])
def searchrating():
    error = ""
    form = GameForm()
    return render_template('searchrating.html', form = form, message = error, chosen_rating = Rating.query.filter_by(name=form.game_name.data).all())

@app.route('/showrating/<int:id>')
def showrating(id):
    game_details = Game.query.filter_by(id=id).first()
    return render_template('showrating.html', chosen_rating = Rating.query.filter_by(name=game_details.name).all())

@app.route('/gamepage')
def gamepage():
    return render_template('gamepage.html', all_games = Game.query.all())

@app.route('/addgame', methods=['GET', 'POST'])
def addgame():
    error=""
    form = AddForm()

    if request.method == 'POST':
        game_name = form.game_name.data
        platform_name = form.platform_name.data
        genre_name = form.genre_name.data

        if len(game_name) == 0 or genre_name == 0:
            error = "Please fill all parts to add a game."
        else:
            new_game = Game(name = game_name, platform = platform_name, genre = genre_name)
            db.session.add(new_game)
            db.session.commit()
            return redirect(url_for("gamepage"))
    return render_template('addgame.html', form = form, message = error)

@app.route('/updatereview/<int:id>', methods=['GET', 'POST'])
def updatereview(id):
    form = GameForm()

    if request.method == "POST":
        review_to_change = Rating.query.filter_by(id=id).first()
        game_review = form.game_review.data
        game_rating = form.game_rating.data
        review_to_change.review = game_review
        review_to_change.rating = game_rating
        db.session.commit()
        return redirect(url_for('gamepage'))
    return render_template('updatereview.html', form=form)

@app.route('/delete/<int:id>')
def delete(id):
    review_to_delete = Rating.query.filter_by(id=id).first()
    db.session.delete(review_to_delete)
    db.session.commit()
    return redirect(url_for("gamepage"))

