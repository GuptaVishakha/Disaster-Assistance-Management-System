import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#this only works with chrome atm
class Iter0Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_iter0(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/")
        self.assertIn("Iteration", driver.title) #this ensures that the word "Iteration" is in the title of the page


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
