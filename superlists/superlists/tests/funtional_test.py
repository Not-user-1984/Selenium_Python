from selenium import webdriver
import unittest


class NewVizitorTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(
            executable_path='/Users/diplug/python _projets/Git My Project/Selenium_Python/superlists/superlists/tests/firefoxdriver/geckodriver')

    def tearDown(self):
        self.driver.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.driver.get('http://localhost:8000')
        title = 'The install worked successfully! Congratulations!'
        self.assertIn(title, self.driver.title)
        self.fail('закончить тест')
