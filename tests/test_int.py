import unittest
import time
from flask import url_for
from urllib.request import urlopen

from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db
from application.models import Game, Rating

class TestBase(LiveServerTestCase):

    def create_app(self):
        """
        Configure the Flask app before every test.
        """
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
        app.config['SECRET_KEY'] = "aodjiwjdoiwja"
        return app

    def setUp(self):
        """
        Setup the test driver and create table schema before every test.
        You can populate the table with some test tasks here if you want to
        test read/update/delete functionality.
        """
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/Islam/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.drop_all()
        db.create_all()

    def tearDown(self):
        """
        Stop the driver after every test.
        """
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        """
        Test that the server is running before each test.
        """
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestGameCreation(TestBase):
    def test_game_creation(self):
        """
        Test that a user can add a game to the Add a Game page,
        enter the name of the game and check to see if
        it redirects to the game page
        """

        # Navigate to the Game page
        self.driver.find_element_by_xpath('/html/body/form[3]/input').click()
        time.sleep(1)
        # Navigate to the Add Game page
        self.driver.find_element_by_xpath('/html/body/form[4]/input').click()
        time.sleep(1)

        # Input the game details into the form fields
        self.driver.find_element_by_xpath('//*[@id="game_name"]').send_keys('Test Game')
        self.driver.find_element_by_xpath('//*[@id="platform_name"]').send_keys('1')
        self.driver.find_element_by_xpath('//*[@id="genre_name"]').send_keys('Test Genre')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(1)

        # Assert that browser redirects to game page
        assert url_for('gamepage') in self.driver.current_url

if __name__ == '__main__':
    unittest.main(port=5000)
