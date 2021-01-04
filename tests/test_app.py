import unittest
from flask import url_for
from flask_testing import TestCase

# import the app's classes and objects
from application import app, db
from application.models import Rating, Game, Game_rating
from application.forms import GameForm, AddForm

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
                SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True
                )
        return app

    def setUp(self):
        db.create_all()

        samplegame1 = Game(name="Test Game", platform = 1, genre = "Test Genre")
        db.session.add(samplegame1)
        db.session.commit()
        
        samplerating1 = Rating(name=samplegame1.name, rating=1, review="Test Review", username="Test_User")
        db.session.add(samplerating1)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()

## Tests that each webpage can be viewed without any errors.
class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_rating_get(self):
        response = self.client.get(url_for('rating'))
        self.assertEqual(response.status_code, 200)

    def test_addrating_get(self):
        response = self.client.get(url_for('addrating'))
        self.assertEqual(response.status_code, 200)
    
    def test_searchrating_get(self):
        response = self.client.get(url_for('searchrating'))
        self.assertEqual(response.status_code, 200)

    def test_showrating_get(self):
        response = self.client.get(url_for('showrating', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_gamepage_get(self):
        response = self.client.get(url_for('gamepage'))
        self.assertEqual(response.status_code, 200)

    def test_addgame_get(self):
        response = self.client.get(url_for('addgame'))
        self.assertEqual(response.status_code, 200)

    def test_updatereview_get(self):
        response = self.client.get(url_for('updatereview', id=1))
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_deletegame_get(self):
        response = self.client.get(url_for('deletegame', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

## Tests all the features are viewed on the homepage & gamepage 
class TestRead(TestBase):
    def test_read_home(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"Welcome, User!", response.data)

    def test_read_gamepage(self):
        response = self.client.get(url_for('gamepage'))
        self.assertIn(b"Test Game", response.data)

## Tests the rating and game is added from the form and that the changes can be viewed on the gamepage & review page.
class TestAdd(TestBase):
    def test_add_rating(self):
        response = self.client.post(
            url_for('addrating'),
            data = dict(game_name="Test Game", game_rating = 5, game_review = "Good test", user_name = "Nice_guy"),
            follow_redirects=True
        )
        self.assertIn(b"Good test", response.data)
        self.assertIn(b"Nice_guy", response.data)

    def test_add_game(self):
        response = self.client.post(
            url_for('addgame'),
            data = dict(game_name = 'Game test', platform_name = 1, genre_name = "Test Genre"),
            follow_redirects=True
        )
        self.assertIn(b"Game test", response.data)
        self.assertIn(b"1", response.data)
        self.assertIn(b"Test Genre", response.data)

## Tests the search form can find the selected reviews and games.
class TestSearch(TestBase):
    def test_search(self):
        response = self.client.post(
            url_for('searchrating'),
            data = dict(game_name = "Test Game"),
            follow_redirects=True
        )
        self.assertIn(b"Test Game", response.data)

## Tests that the user can update the selected review.
class TestUpdate(TestBase):
    def test_update_review(self):
        response = self.client.post(
            url_for('updatereview', id=1),
            data = dict(game_review = 'Changed review', game_rating = 2),
            follow_redirects=True
        )
        self.assertIn(b"Changed review", response.data)
        self.assertIn(b"2", response.data)

## Tests the selected data is deleted from the table and is no longer viewable on the game and review page.
class TestDelete(TestBase):
    def test_delete_review(self):
        response = self.client.post(
            url_for('delete', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test Review", response.data)

    def test_delete_game(self):
        response = self.client.post(
            url_for('deletegame', id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"Test Game", response.data)
