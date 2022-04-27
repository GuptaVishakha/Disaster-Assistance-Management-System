from iteration1 import createPledge
from selenium import webdriver
import mysql.connector
from selenium.webdriver.support.ui import Select
import unittest

class Iter1Search(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()


    def test_successfulrequest(self):
        driver = self.driver

        mydb = mysql.connector.connect(host="localhost", user="root", password="team06", database="sys")
        cursor = mydb.cursor(buffered=True)

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr3")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/pledge")
        name = driver.find_element_by_id("Name")
        loc = driver.find_element_by_id("Location")

        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        box4 = driver.find_element_by_id("Money")
        desc = driver.find_element_by_id("description")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant4 = driver.find_element_by_id("Moneyquantity")

        box1.click()
        box2.click()
        box3.click()
        box4.click()
        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        quant4.send_keys("3")
        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")
        name.send_keys("JOHN SMITH")
        loc.send_keys("nowhere")

        submit = driver.find_element_by_name("submit")
        submit.click()
        cursor.execute("DELETE FROM pledge WHERE username = 'mchr3'")
        mydb.commit()
        self.assertIn("pledge Created Successfully",driver.page_source)

    def test_missingdesc(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/pledge")
        loc = driver.find_element_by_id("Location")
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        box4 = driver.find_element_by_id("Money")
        desc = driver.find_element_by_id("description")
        name = driver.find_element_by_id("Name")
        quant1 = driver.find_element_by_id("Waterquantity")
        quant2 = driver.find_element_by_id("Foodquantity")
        quant3 = driver.find_element_by_id("Clothingquantity")
        quant4 = driver.find_element_by_id("Moneyquantity")

        box1.click()
        box2.click()
        box3.click()
        box4.click()

        quant1.send_keys("11")
        quant2.send_keys("22")
        quant3.send_keys("5")
        quant4.send_keys("3")
        name.send_keys("JOHN SMITH")
        loc.send_keys("nowhere")
        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("Create Pledge", driver.title)

    def test_nobox(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/auth/login")
        userbox = driver.find_element_by_id("user")
        passbox = driver.find_element_by_id("password")
        userbox.send_keys("mchr")
        passbox.send_keys("Team06!66")
        submit = driver.find_element_by_id("submit")
        submit.click()

        driver.get("http://127.0.0.1:5000/home/pledge")

        loc = driver.find_element_by_id("Location")
        box1 = driver.find_element_by_id("Water")
        box2 = driver.find_element_by_id("Food")
        box3 = driver.find_element_by_id("Clothing")
        desc = driver.find_element_by_id("description")
        name = driver.find_element_by_id("Name")

        desc.send_keys("THIS IS A DESCRIPTION FOR THE REQUEST CURRENTLY BEING MADE")
        name.send_keys("JOHN SMITH")
        loc.send_keys("nowhere")
        submit = driver.find_element_by_name("submit")
        submit.click()

        self.assertIn("No Items Selected", driver.page_source)




    def tearDown(self):

        self.driver.close()


if __name__ == "__main__":
    unittest.main()